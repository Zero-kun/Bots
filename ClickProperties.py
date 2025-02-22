import win32api
import time

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)

state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button up = 0 or 1. Button down = -127 or -128
    
while keyboard.is_pressed('q') == False:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
        
    if b != state_right:  # Button state changed
        state_right = b
        print(b)
        
        if b < 0:
            print('Right Button Pressed')
        else:
            print('Right Button Released')
            win32api.SetCursorPos((midWidth, 50))