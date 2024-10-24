# merger.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DocumentMerger:
    def __init__(self, master):
        self.master = master
        self.files = []
        self.setup_ui()
        # Auto-load will now happen when switching to the merger tab

    def setup_ui(self):
        file_frame = ttk.Frame(self.master)
        file_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.file_listbox = tk.Listbox(file_frame, width=70, height=10)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(file_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        button_frame = ttk.Frame(self.master)
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Button(button_frame, text="Add Files", command=self.add_files).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Merge Files", command=self.merge_files).pack(side=tk.LEFT, padx=5)

    def auto_load_last_processed(self):
        try:
            # Get reference to the processor instance through the notebook
            notebook = self.master.master
            processor = notebook.children['!frame2'].children['!documentprocessor']
            
            if processor and processor.last_output_folder and os.path.exists(processor.last_output_folder):
                self.clear_all()
                files = []
                for filename in os.listdir(processor.last_output_folder):
                    if filename.endswith('.html'):
                        full_path = os.path.join(processor.last_output_folder, filename)
                        files.append((self.get_sort_key(filename), full_path))
                
                # Sort files naturally
                files.sort(key=lambda x: x[0])
                
                # Add sorted files to the listbox
                for _, file_path in files:
                    self.files.append(file_path)
                    self.file_listbox.insert(tk.END, os.path.basename(file_path))
        except Exception as e:
            print(f"Error auto-loading last processed files: {e}")

    def get_sort_key(self, filename):
        import re
        parts = re.split('([0-9]+)', os.path.splitext(filename)[0])
        parts = [int(part) if part.isdigit() else part.lower() for part in parts]
        return parts

    def add_files(self):
        files = filedialog.askopenfilenames(filetypes=[("HTML Files", "*.html")])
        for file in files:
            self.files.append(file)
            self.file_listbox.insert(tk.END, os.path.basename(file))

    def remove_selected(self):
        selection = self.file_listbox.curselection()
        for index in reversed(selection):
            del self.files[index]
            self.file_listbox.delete(index)

    def clear_all(self):
        self.files.clear()
        self.file_listbox.delete(0, tk.END)

    def merge_files(self):
        if not self.files:
            messagebox.showerror("Error", "Please add files to merge.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".html",
                                                  filetypes=[("HTML files", "*.html")])
        if not output_file:
            return

        try:
            # Read the first file to get its head content
            with open(self.files[0], 'r', encoding='utf-8') as first_file:
                first_content = first_file.read()
                head_start = first_content.find("<head")
                head_end = first_content.find("</head>") + 7
                if head_start != -1 and head_end != -1:
                    head_content = first_content[head_start:head_end]
                else:
                    head_content = "<head><meta charset='UTF-8'></head>"

            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write("<!DOCTYPE html>\n<html lang='en'>\n")
                # Insert the head content and add print-specific CSS
                outfile.write(head_content.replace("</head>", """
                    <style>
                        @media print {
                            @page {
                                size: A4;
                                margin: 2cm;
                            }
                            body {
                                margin: 0;
                                padding: 0;
                            }
                            /* Force page breaks between sections */
                            .section-break {
                                page-break-before: always;
                            }
                        }
                    </style>
                    </head>
                """))
                outfile.write("<body>\n")

                for i, file in enumerate(self.files):
                    with open(file, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        # Extract only the body content
                        body_start = content.find("<body")
                        if body_start != -1:
                            body_start = content.find(">", body_start) + 1
                            body_end = content.find("</body>")
                            if body_end != -1:
                                content = content[body_start:body_end]
                        
                        # Add section break div before content (except for first file)
                        if i > 0:
                            outfile.write('<div class="section-break"></div>\n')
                        outfile.write(content + "\n")

                outfile.write("</body>\n</html>")

            # Convert to PDF using Chrome
            pdf_file = output_file.rsplit('.', 1)[0] + '.pdf'
            
            chrome_options = Options()
            chrome_options.add_argument('--headless=new')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')

            try:
                service = Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service, options=chrome_options)
                
                # Load the merged HTML file
                driver.get(f'file:///{os.path.abspath(output_file)}')
                
                # Wait for any dynamic content to load
                driver.implicitly_wait(2)

                # Print to PDF with proper page settings
                print_options = {
                    'landscape': False,
                    'displayHeaderFooter': False,
                    'printBackground': True,
                    'preferCSSPageSize': True,
                }

                pdf_data = driver.execute_cdp_cmd('Page.printToPDF', print_options)
                
                # Save the PDF file
                with open(pdf_file, 'wb') as f:
                    f.write(base64.b64decode(pdf_data['data']))

                messagebox.showinfo("Success", 
                    f"Files merged successfully!\nHTML: {output_file}\nPDF: {pdf_file}")
                
            finally:
                driver.quit()

        except Exception as e:
            messagebox.showerror("Error", f"Error merging files: {str(e)}")
