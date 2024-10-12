from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from custom_widgets import CustomButton, CustomLabel, CustomTextInput, CustomFileChooser

import os
import datetime
from docx import Document
import win32com.client
import pythoncom
import uuid

class DocumentSplitter(BoxLayout):
    on_split_complete = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20
        self.filename = None
        self.title_structure = []

        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        grid.add_widget(CustomLabel(text="Select File:"))
        self.upload_button = CustomButton(text="Upload Word or PDF File", on_press=self.show_file_chooser)
        grid.add_widget(self.upload_button)

        grid.add_widget(CustomLabel(text="Depth Level:"))
        self.depth_slider = Slider(min=1, max=9, value=1, step=1, size_hint=(1, None), height=40)
        self.depth_slider.bind(value=self.update_tree)
        grid.add_widget(self.depth_slider)

        self.add_widget(grid)

        self.tree = TreeView(hide_root=True, size_hint_y=None, height=300)
        self.add_widget(self.tree)

        self.split_button = CustomButton(text="Split Document and Save", on_press=self.split_document)
        self.add_widget(self.split_button)

    def show_file_chooser(self, instance):
        content = BoxLayout(orientation='vertical')
        file_chooser = CustomFileChooser(filters=['*.docx', '*.pdf'])
        content.add_widget(file_chooser)
        
        select_button = CustomButton(text="Select")
        select_button.bind(on_press=lambda x: self.upload_file(file_chooser.selection))
        content.add_widget(select_button)
        
        popup = Popup(title="Choose a file", content=content, size_hint=(0.9, 0.9))
        select_button.bind(on_press=popup.dismiss)
        popup.open()

    def upload_file(self, selection):
        if selection:
            self.filename = selection[0]
            if self.filename.lower().endswith('.pdf'):
                word_filename = self.convert_pdf_to_word(self.filename)
                if word_filename:
                    self.filename = word_filename
                else:
                    self.show_error("Failed to convert PDF to Word.")
                    return
            self.analyze_document()
        else:
            self.show_error("No file selected.")

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
            self.show_error(f"Failed to analyze the document: {str(e)}")

    def update_tree(self, *args):
        self.tree.clear_widgets()
        depth = int(self.depth_slider.value)
        parent_stack = [None]
        last_level = 0

        for item in self.title_structure:
            level = item['level']
            text = item['text']
            if level <= depth:
                while level <= last_level:
                    parent_stack.pop()
                    last_level -= 1
                parent = parent_stack[-1]
                current_node = self.tree.add_node(TreeViewLabel(text=text), parent)
                parent_stack.append(current_node)
                last_level = level

    def split_document(self, instance):
        if not self.filename:
            self.show_error("Please upload a document first.")
            return

        depth = int(self.depth_slider.value)
        try:
            doc = Document(self.filename)
            script_dir = os.path.dirname(os.path.abspath(__file__))
            base_name = os.path.splitext(os.path.basename(self.filename))[0]
            output_folder = os.path.join(script_dir, f"{base_name}_split_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
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
                unique_id = str(uuid.uuid4())[:8]
                output_filename = os.path.join(output_folder, f"{idx+1}_{unique_id}.docx")
                section['document'].save(output_filename)

            self.show_info(f"Document split into {len(sections)} sections and saved in {output_folder}")
            if self.on_split_complete:
                self.on_split_complete(self, output_folder)
        except Exception as e:
            self.show_error(f"An error occurred while splitting the document: {str(e)}")

    def show_error(self, message):
        popup = Popup(title='Error', content=CustomLabel(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_info(self, message):
        popup = Popup(title='Information', content=CustomLabel(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
