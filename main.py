from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.lang import Builder
from kivy.core.window import Window

from splitter import DocumentSplitter
from processor import DocumentProcessor
from merger import DocumentMerger

Builder.load_string('''
#:import hex kivy.utils.get_color_from_hex

<IntegratedApp>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: hex('#E6F3FF')
        Rectangle:
            pos: self.pos
            size: self.size
    
    TabbedPanel:
        do_default_tab: False
        background_color: hex('#3498DB')
        
        TabbedPanelItem:
            text: 'Splitter'
            background_color: hex('#2980B9')
            DocumentSplitter:
                id: splitter
        
        TabbedPanelItem:
            text: 'Processor'
            background_color: hex('#2980B9')
            DocumentProcessor:
                id: processor
        
        TabbedPanelItem:
            text: 'Merger'
            background_color: hex('#2980B9')
            DocumentMerger:
                id: merger
''')

class IntegratedApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.splitter.bind(on_split_complete=self.on_split_complete)

    def on_split_complete(self, instance, output_folder):
        self.ids.processor.load_split_files(output_folder)

class DocumentProcessorApp(App):
    def build(self):
        Window.size = (800, 600)
        return IntegratedApp()

if __name__ == '__main__':
    DocumentProcessorApp().run()
