import kivy
import os
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

kivy.require('1.11.1')

# Font for Label
LabelBase.register('Arial_Rounded_Bold', fn_regular=os.path.join(os.path.dirname(__file__),
                                                                 'Font/Arial_Rounded_Bold.ttf'))


class PopupWindow(FloatLayout):
    pass


def popup_show():
    pop = PopupWindow()

    pop_win = Popup(title="Analysis", content=pop, size_hint=(None, None), size=(1600, 800))
    pop_win.open()


class SearchPerformer(BoxLayout):
    def hit_enter(self):
        popup_show()


class PriceTrackerUIApp(App):
    def build(self):
        return SearchPerformer()
