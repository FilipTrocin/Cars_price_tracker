from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
import UI

Window.size = (866, 412)

UI.PriceTrackerUIApp().run()