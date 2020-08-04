import kivy
import os
from kivy.app import App
from kivy.app import Widget
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle


kivy.require('1.11.1')


def on_enter(value):
    lista = []
    lista.append(value)


# Font for TextInput
LabelBase.register('Arial_Rounded_Bold', fn_regular=os.path.join(os.path.dirname(__file__),
                                                                 'Font/Arial_Rounded_Bold.ttf'))


class CanvasWidget(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return CanvasWidget()
