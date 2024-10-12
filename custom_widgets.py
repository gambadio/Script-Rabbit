from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.graphics import Color, Rectangle

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.2, 0.6, 0.8, 1)  # Equivalent to hex('#3498DB')
        self.background_normal = ''
        self.color = (1, 1, 1, 1)  # White text
        self.size_hint = (None, None)
        self.size = (180, 40)
        self.font_size = '14sp'

class CustomLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0.17, 0.24, 0.31, 1)  # Equivalent to hex('#2C3E50')
        self.font_size = '14sp'
        self.size_hint_x = None
        self.width = 150
        self.text_size = self.size
        self.halign = 'right'
        self.valign = 'middle'

class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1, 1, 1, 1)  # White background
        self.foreground_color = (0.17, 0.24, 0.31, 1)  # Equivalent to hex('#2C3E50')
        self.cursor_color = (0.2, 0.6, 0.8, 1)  # Equivalent to hex('#3498DB')
        self.font_size = '14sp'
        self.size_hint = (1, None)
        self.height = 40
        self.multiline = False

class CustomFileChooser(FileChooserListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.dirselect = True

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
