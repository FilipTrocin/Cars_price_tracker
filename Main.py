from kivy.properties import get_color_from_hex
from kivy.core.window import Window
import UI
import Database

Window.size = (800, 390)
Window.clearcolor = get_color_from_hex('#F9E29C')
UI.PriceTrackerUIApp().run()