import kivy
import os
from kivy.app import App
from kivy.app import Widget
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

kivy.require('1.11.1')

# Font for TextInput
LabelBase.register('Arial_Rounded_Bold', fn_regular=os.path.join(os.path.dirname(__file__),
                                                                 'Font/Arial_Rounded_Bold.ttf'))


class PopupWindow(FloatLayout):
    @staticmethod
    def popup_show():
        pop = Popup(title="Analysis", content=PopupWindow, size_hint=(None, None), size=(500, 500))
        pop.open()


class CanvasWidget(BoxLayout):
    pass


class AmazonPriceTrackerApp(App):
    def build(self):
        return CanvasWidget()
