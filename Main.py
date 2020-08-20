from kivy.properties import get_color_from_hex
from kivy.core.window import Window
import UI

Window.size = (683, 263)
Window.clearcolor = get_color_from_hex('#F9E29C')
UI.PriceTrackerUIApp().run()