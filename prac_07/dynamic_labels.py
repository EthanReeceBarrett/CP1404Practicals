"""Simple program used to show dynamic lables"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Constructs Main app"""
        super().__init__(**kwargs)
        self.names = ("Bob Brown", "Cat Cyan", "Oren Ochre")

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_list.add_widget(temp_label)


DynamicLabelsApp().run()
