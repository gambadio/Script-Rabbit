import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import datetime
from docx import Document
import win32com.client
import pythoncom

class DocumentSplitter:
    def __init__(self, master):
        self.master = master
        self.filename = None
        self.title_structure = []
        self.setup_ui()

    def setup_ui(self):
        self.upload_button = tk.Button(self.master, text="Upload Word or PDF File", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.depth_level = tk.IntVar(value=1)
        self.depth_slider = tk.Scale(self.master, from_=1, to=9, orient=tk.HORIZONTAL, label="Depth Level", 
                                     variable=self.depth_level, command=self.update_tree)
        self.depth_slider.pack(pady=10)

        self.tree = ttk.Treeview(self.master)
        self.tree.heading("#0", text="Title Structure")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.split_button = tk.Button(self.master, text="Split Document and Save", command=self.split_document)
        self.split_button.pack(pady=10)

    def upload_file(self):
        filetypes = [('Word Documents', '*.docx'), ('PDF Files', '*.pdf'), ('All files', '*.*')]
        filename = filedialog.askopenfilename(title='Open a file', filetypes=filetypes)
        if filename:
            self.filename = filename
            if filename.lower().endswith('.pdf'):
                word_filename = self.convert_pdf_to_word(filename)
                if word_filename:
                    self.filename = word_filename
                else:
                    messagebox.showerror("Error", "Failed to convert PDF to Word.")
                    return
            self.analyze_document()
        else:
            messagebox.showinfo("No file selected", "Please select a file to upload.")

    def convert_pdf_to_word(self, pdf_filename):
        try:
            pythoncom.CoInitialize()
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False

            pdf_path = os.path.abspath(pdf_filename)
            doc = word.Documents.Open(pdf_path)

            word_filename = pdf_filename[:-4] + '.docx'
            doc.SaveAs2(os.path.abspath(word_filename), FileFormat=16)
            doc.Close()
            word.Quit()
            return word_filename
        except Exception as e:
            print(f"Error converting PDF to Word: {e}")
            return None
        finally:
            pythoncom.CoUninitialize()

    def analyze_document(self):
        try:
            doc = Document(self.filename)
            self.title_structure = []

            for para in doc.paragraphs:
                style = para.style.name
                text = para.text.strip()
                if text and style.startswith('Heading'):
                    try:
                        level = int(style.replace('Heading ', ''))
                    except:
                        level = 1
                    self.title_structure.append({'level': level, 'text': text})

            self.update_tree()
        except Exception as e:
            print(f"Error analyzing document: {e}")
            messagebox.showerror("Error", "Failed to analyze the document.")

    def update_tree(self, event=None):
        self.tree.delete(*self.tree.get_children())
        depth = self.depth_level.get()
        parent_stack = [""]
        last_level = 0

        for item in self.title_structure:
            level = item['level']
            text = item['text']
            if level <= depth:
                while level <= last_level:
                    parent_stack.pop()
                    last_level -= 1
                parent = parent_stack[-1]
                current_node = self.tree.insert(parent, 'end', text=text)
                parent_stack.append(current_node)
                last_level = level

    def split_document(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload a document first.")
            return

        depth = self.depth_level.get()
        try:
            doc = Document(self.filename)
            base_dir = os.path.dirname(self.filename)
            base_name = os.path.splitext(os.path.basename(self.filename))[0]
            output_folder = os.path.join(base_dir, f"{base_name}_split_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
            os.makedirs(output_folder)

            sections = []
            current_doc = None
            current_level = 0
            current_title = ""

            for para in doc.paragraphs:
                style = para.style.name
                text = para.text.strip()
                if text:
                    if style.startswith('Heading'):
                        try:
                            level = int(style.replace('Heading ', ''))
                        except:
                            level = 1
                        if level <= depth:
                            if current_doc:
                                sections.append({'level': current_level, 'title': current_title, 'document': current_doc})
                            current_doc = Document()
                            current_doc.add_paragraph(text, style=style)
                            current_level = level
                            current_title = text
                        else:
                            if current_doc:
                                current_doc.add_paragraph(text, style=style)
                    else:
                        if current_doc:
                            current_doc.add_paragraph(text, style=style)

            if current_doc:
                sections.append({'level': current_level, 'title': current_title, 'document': current_doc})

            for idx, section in enumerate(sections):
                title = section['title']
                filename_safe_title = ''.join(c for c in title if c.isalnum() or c in ' _-').rstrip()
                output_filename = os.path.join(output_folder, f"{idx+1}_{filename_safe_title}.docx")
                section['document'].save(output_filename)

            messagebox.showinfo("Success", f"Document split into {len(sections)} sections and saved in {output_folder}")
        except Exception as e:
            print(f"Error splitting document: {e}")
            messagebox.showerror("Error", "An error occurred while splitting the document.")
