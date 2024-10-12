# integrated_app.py
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from splitter import SplitterScreen
from processor import ProcessorScreen
from merger import MergerScreen

Builder.load_string('''
<IntegratedApp>:
    MDTabs:
        id: tabs
        on_tab_switch: root.on_tab_switch(*args)
        Tab:
            title: "Splitter"
            SplitterScreen:
                id: splitter_screen
        Tab:
            title: "Processor"
            ProcessorScreen:
                id: processor_screen
        Tab:
            title: "Merger"
            MergerScreen:
                id: merger_screen

<Tab>:
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            id: tab_label
            text: root.title
            halign: 'center'
        
''')

class Tab(MDBoxLayout, MDTabsBase):
    pass

class IntegratedApp(MDScreen):
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        pass  # You can handle tab switch events here
