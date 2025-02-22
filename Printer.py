import pyautogui
import time

time.sleep(2)

im1 = pyautogui.screenshot(region=(505,410,1340-505,945-410))
im1.save(r"./savedimage.png")
#pyautogui.displayMousePosition()
#X:  506 Y:  412 RGB: (  0,  34,  56)
#X: 1398 Y:  946 RGB: (  0,  34,  56)
