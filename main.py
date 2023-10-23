import pyautogui
from time import sleep
import keyboard
sleep(2)
for i in range(1,100):Hello world
    sleep(1)
    pyautogui.write("Hello world\n")
    if keyboard.is_pressed('q'):
        print("You pressed 'q', breaking the loop.")
        break