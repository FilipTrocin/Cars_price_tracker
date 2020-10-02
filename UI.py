import os
import kivy
import database
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.uix.tabbedpanel import TabbedPanel

kivy.require('1.11.1')

# Fonts for Label
LabelBase.register('Arial_Rounded_Bold', fn_regular=os.path.join(os.path.dirname(__file__),
                                                                 'Fonts/Arial_Rounded_Bold.ttf'))
LabelBase.register('AmericanTypewriter', fn_regular=os.path.join(os.path.dirname(__file__),
                                                                 'Fonts/AmericanTypewriter.ttc'))
user_input = []


class PopupWindow(TabbedPanel):
    forward = ObjectProperty(None)

    daily = StringProperty('./daily.png')
    weekly = StringProperty('./weekly.png')
    button = StringProperty('./Graphics/iu.png')

    analysis = ListProperty(database.daily_analysis)


def popup_show():
    pop = PopupWindow()
    pop_win = ModalView(border=(16, 32, 16, 32), size_hint=(.99, .93))
    pop_win.add_widget(pop)

    pop_win.open()
    return pop  # saving a reference to DailyPopup()


class SearchPerformer(BoxLayout):
    dt = database
    pop = ObjectProperty(None)

    def hit_enter(self):
        self.pop = popup_show()

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
            if self.pop is not None:  # If PopupWindow exists
                self.pop.ids.img.reload()
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

