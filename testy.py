import os
import kivy
import database
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.uix.tabbedpanel import TabbedPanel

images = ['./daily.png', './daily1.png']


class Picture(BoxLayout):
    source = StringProperty(None)


class Test(BoxLayout):
    image = StringProperty(images[0])
    index = NumericProperty(0)

    def hit_button(self):
        self.index += 1
        self.index %= len(images)
        self.image = images[self.index]


def display():
    for filename in images:
        pic = Picture(source=filename)


class MainApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    MainApp().run()