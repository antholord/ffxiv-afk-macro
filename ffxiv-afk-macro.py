import keyboard
import random
import time
from pywinauto import Application
app = Application().connect(title="FINAL FANTASY XIV", visible_only=False, top_level_only=False, enabled_only=False)
print("FFXIV AFK MACRO :: CONNECTED")
while True:
      print("FFXIV AFK MACRO :: WAKING UP")
      app.top_window().set_focus()
      keyboard.press_and_release('d')
      time.sleep(random.randint(1, 3))
      keyboard.press_and_release('a')
      time.sleep(random.randint(60, 400))