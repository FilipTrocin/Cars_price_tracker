import kivy
import os
from kivy.app import App
from kivy.app import Widget
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
import matplotlib.pyplot as plt
import bottlenose as bt

kivy.require('1.11.1')


def on_enter(value):
    lista = []
    lista.append(value)


# Font for TextInput
LabelBase.register('Arial_Rounded_Bold', fn_regular=os.path.join(os.path.dirname(__file__),
                                                                 'Font/Arial_Rounded_Bold.ttf'))


class GraphicalApp(Widget):
    pass
    # def __init__(self, **kwargs):
    #     super(GraphicalApp, self).__init__(**kwargs)
    #     self.size = (900, 70)
    #     self.text_in = TextInput(multiline=False, font_name=os.path.join(os.path.dirname(__file__),
    #                                                                      'Font/Arial_Rounded_Bold.ttf'))
    #     self.add_widget(self.text_in)


class Application(App):
    def build(self):
        return FloatLayout()
