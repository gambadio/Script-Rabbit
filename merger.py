import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

class DocumentMerger:
    def __init__(self, master):
        self.master = master
        self.files = []
        self.setup_ui()

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
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Merged Document</title>
                </head>
                <body>
                """)

                for file in self.files:
                    with open(file, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)

                outfile.write("""
                </body>
                </html>
                """)

            messagebox.showinfo("Success", f"Files merged successfully into {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error merging files: {str(e)}")
