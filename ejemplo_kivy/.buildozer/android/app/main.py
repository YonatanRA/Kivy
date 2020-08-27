from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class btnToast(Button):
    text = 'Toast'
    def on_press(self):
        print('QUIERO MOSTRAR UN TOAST')

class btnShare(Button):
    text = 'Share'
    def on_press(self):
        print('QUIERO COMPARTIR UN TEXTO POR WHATSAPP')

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
