from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from custom_widgets import CustomButton, CustomLabel, CustomTextInput, CustomFileChooser

import os
import json
from anthropic import Anthropic
from docx import Document

class DocumentProcessor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20
        self.anthropic = None
        self.prompts = self.load_default_prompts()
        self.current_prompt = "Default"
        self.files = []

        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        grid.add_widget(CustomLabel(text='Anthropic API Key:'))
        self.api_key_input = CustomTextInput(password=True)
        grid.add_widget(self.api_key_input)

        grid.add_widget(CustomLabel(text=''))
        self.set_api_button = CustomButton(text='Set API Key', on_press=self.set_api_key)
        grid.add_widget(self.set_api_button)

        grid.add_widget(CustomLabel(text='Files to Process:'))
        self.file_list = CustomTextInput(readonly=True, multiline=True)
        grid.add_widget(self.file_list)

        grid.add_widget(CustomLabel(text='Output Folder:'))
        self.output_folder = CustomTextInput()
        grid.add_widget(self.output_folder)

        grid.add_widget(CustomLabel(text='Current Prompt:'))
        self.prompt_spinner = Spinner(text='Default', values=list(self.prompts.keys()), size_hint=(1, None), height=40)
        self.prompt_spinner.bind(text=self.on_prompt_selected)
        grid.add_widget(self.prompt_spinner)

        self.add_widget(grid)

        self.process_button = CustomButton(text='Process Files', on_press=self.process_files)
        self.add_widget(self.process_button)

    def load_default_prompts(self):
        return {
            "Default": "Your default prompt here"
        }

    def set_api_key(self, instance):
        api_key = self.api_key_input.text
        if api_key:
            try:
                self.anthropic = Anthropic(api_key=api_key)
                self.show_info('API Key set successfully!')
            except Exception as e:
                self.show_error(f"Error setting API Key: {str(e)}")
        else:
            self.show_error("Please enter an API Key.")

    def load_split_files(self, folder_path):
        self.files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.docx')]
        self.file_list.text = "\n".join(self.files)
        self.output_folder.text = os.path.join(folder_path, 'processed')

    def on_prompt_selected(self, spinner, text):
        self.current_prompt = text

    def process_files(self, instance):
        if not self.anthropic:
            self.show_error("Please set your Anthropic API Key first.")
            return

        if not self.files:
            self.show_error("No files to process.")
            return

        output_folder = self.output_folder.text
        if not output_folder:
            self.show_error("Please specify an output folder.")
            return

        os.makedirs(output_folder, exist_ok=True)

        for file in self.files:
            try:
                doc = Document(file)
                content = "\n".join([para.text for para in doc.paragraphs])
                
                response = self.anthropic.messages.create(
                    model="claude-3-5-sonnet-20240620",
                    max_tokens=8000,
                    temperature=0.7,
                    system=self.prompts[self.current_prompt],
                    messages=[
                        {"role": "user", "content": f"Please process this content: {content}"}
                    ],
                    extra_headers={"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}
                )

                output_content = response.content[0].text if response.content else ""
                
                output_file = os.path.join(output_folder, f"processed_{os.path.basename(file)}.html")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(output_content)

            except Exception as e:
                self.show_error(f"Error processing file {file}: {str(e)}")

        self.show_info("All files processed successfully!")

    def show_error(self, message):
        popup = Popup(title='Error', content=CustomLabel(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_info(self, message):
        popup = Popup(title='Information', content=CustomLabel(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
