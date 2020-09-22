import os
import kivy
import database
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

kivy.require('1.11.1')

# Font for Label
LabelBase.register('Arial_Rounded_Bold', fn_regular=os.path.join(os.path.dirname(__file__),
                                                                 'Font/Arial_Rounded_Bold.ttf'))

user_input = []


class PopupWindow(FloatLayout):
    pass


def popup_show():
    pop = PopupWindow()

    pop_win = Popup(title="Analysis", content=pop, size_hint=(None, None), size=(1500, 700))
    pop_win.open()


class SearchPerformer(BoxLayout):
    dt = database

    def hit_enter(self):
        popup_show()

    def input_grabber(self, database):
        specs = [self.ids.crmk.text, self.ids.crmd.text, self.ids.cryr.text, self.ids.crft.text]
        trimmed = [item.strip() for item in specs]
        lowered = [item.lower() for item in trimmed]
        try:
            int(self.ids.cryr.text)
            user_input.extend(lowered)
            database.add_to_database()
            database.query_database()
            database.run_plot()
            user_input.clear()
        except ValueError:
            user_input.clear()
            print('You did not provide a car year')

    def clear(self):
        self.ids.crmk.text = ""
        self.ids.crmd.text = ""
        self.ids.cryr.text = ""
        self.ids.crft.text = ""


class PriceTrackerUIApp(App):
    def build(self):
        return SearchPerformer()
