from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from custom_widgets import CustomButton, CustomLabel, CustomTextInput, CustomFileChooser
import os

class DocumentMerger(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20
        self.files = []

        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        grid.add_widget(CustomLabel(text='Files to Merge:'))
        self.file_list = CustomTextInput(readonly=True, multiline=True)
        grid.add_widget(self.file_list)

        self.add_widget(grid)

        button_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)
        self.add_files_button = CustomButton(text='Add Files', on_press=self.show_file_chooser)
        self.remove_selected_button = CustomButton(text='Remove Selected', on_press=self.remove_selected)
        self.clear_all_button = CustomButton(text='Clear All', on_press=self.clear_all)
        self.merge_button = CustomButton(text='Merge Files', on_press=self.merge_files)

        button_layout.add_widget(self.add_files_button)
        button_layout.add_widget(self.remove_selected_button)
        button_layout.add_widget(self.clear_all_button)
        button_layout.add_widget(self.merge_button)

        self.add_widget(button_layout)

    def show_file_chooser(self, instance):
        content = BoxLayout(orientation='vertical')
        file_chooser = CustomFileChooser(filters=['*.html'])
        content.add_widget(file_chooser)
        
        select_button = CustomButton(text="Select")
        select_button.bind(on_press=lambda x: self.add_files(file_chooser.selection))
        content.add_widget(select_button)
        
        popup = Popup(title="Choose files", content=content, size_hint=(0.9, 0.9))
        select_button.bind(on_press=popup.dismiss)
        popup.open()

    def add_files(self, selection):
        for file in selection:
            if file not in self.files:
                self.files.append(file)
        self.update_file_list()

    def remove_selected(self, instance):
        # In a real implementation, you'd have a way to select files.
        # For simplicity, we'll just remove the last file.
        if self.files:
            self.files.pop()
        self.update_file_list()

    def clear_all(self, instance):
        self.files.clear()
        self.update_file_list()

    def update_file_list(self):
        self.file_list.text = "\n".join(self.files)

    def merge_files(self, instance):
        if not self.files:
            self.show_error("No files to merge.")
            return

        output_file = self.get_save_path()
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

            self.show_info(f"Files merged successfully into {output_file}")
        except Exception as e:
            self.show_error(f"Error merging files: {str(e)}")

    def get_save_path(self):
        content = BoxLayout(orientation='vertical')
        file_chooser = CustomFileChooser(filters=['*.html'], mode='save')
        content.add_widget(file_chooser)
        
        save_button = CustomButton(text="Save")
        content.add_widget(save_button)
        
        popup = Popup(title="Save merged file", content=content, size_hint=(0.9, 0.9))
        
        def on_save(instance):
            if file_chooser.selection:
                popup.dismiss()
        
        save_button.bind(on_press=on_save)
        popup.open()
        
        return file_chooser.selection[0] if file_chooser.selection else None

    def show_error(self, message):
        popup = Popup(title='Error', content=CustomLabel(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_info(self, message):
        popup = Popup(title='Information', content=CustomLabel(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
