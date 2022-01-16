import pyautogui
import keyboard
from PIL import Image

i = 1
print('Running .... ')
while True:
    if keyboard.read_key() == "x":
        pyautogui.screenshot("screenshot" + str(i) + ".png")
        print("take screenshot"+" screenshot" + str(i) + ".png")
        # break
        im = Image.open("screenshot" + str(i) + ".png")
        # im1 = im.crop((1220,234,1545,604))
        im1 = im.crop((1237,204,1637,654))
        im1.save("screenshot" + str(i) + ".png")
        i += 1
