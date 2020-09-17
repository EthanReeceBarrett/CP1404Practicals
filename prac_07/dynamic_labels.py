"""Simple program used to show dynamic lables"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Constructs Main app"""
        super().__init__(**kwargs)
        self.names = ("Bob Brown", "Cat Cyan", "Oren Ochre")

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root


DynamicLabelsApp().run()