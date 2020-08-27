from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import second # Módulo second (second.py) que definiremos a continuación


class btnToast(Button):
    text = 'Toast'
    def on_press(self):
        second.toast('Toast generado con pyjnius') # Método second.toast que definiremos a continuación

class btnShare(Button):
    text = 'Share'
    def on_press(self):
        second.share('Texto comparitdo con pyjnius') # Método second.share que definiremos a continuación

class Box(BoxLayout):
    orientation = 'vertical'
    def __init__(self):
        super(Box, self).__init__()
        self.add_widget(btnToast())
        self.add_widget(btnShare())

class MainApp(App):
    def build(self):
        return Box()


if __name__ == "__main__":
    MainApp().run()
