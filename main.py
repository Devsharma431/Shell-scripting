import pyautogui
import keyboard 
from time import sleep
sleep(3)
for i in range(100):
    pyautogui.write("Hello This is Dev sharma")
    if keyboard.is_pressed('q'):
        break