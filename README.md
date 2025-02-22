# Programming

#### Some few simple "bots" for grinding boring games. Mobile or on the computer.

---------------------------------------------------------------------------------------

#### The scripts ("bots") shall:
  - be as light as possible;
  - run purely on Python; and
  - be limited in imports to pyautogui,
  time, keyboard, random, win32api, win32con.

#### Exceptions:
  - adb, to be used to mirror the screen from Android smartphones on a PC; and
  - bash to script adb shell inputs to control the device.

Note: all scripts shall work on mobile. Most scripts here will require screen 
mirroring and mouse control to grind the games. Currently, none of the scripts 
will work directly on the smartphone, but that will be done at some time.

---------------------------------------------------------------------------------------

#### Reasons for the aforementioned imports:

##### import time
  - Sleep function: Makes it possible to add a delay between clicks and between screenshots, reducing the impact on the machine's speed
  - Maybe it could also be used to calculate the time between in-game events. 
##### import win32api, win32con
  - Used to control the mouse, get its position, and register when the mouse's buttons are clicked.   
##### import keyboard
  - Used to type keys or identify typed keys.  
##### import random
  - Used to make things random (less "bot-like"). Can randomize pause between clicks, typing, mouse position, sequence of actions, etc.   
##### import pyautogui
  - The magic behind it all. Takes screenshots, identifies pixel colors, recognizes images, etc.
  - Basically, it is the soul that makes this project possible.
