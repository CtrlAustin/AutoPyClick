# Python program to take
# screenshots


import numpy as np
import cv2
import pyautogui
import imagehash
import time
from PIL import Image

# take screenshot
#image = pyautogui.screenshot()

# since the pyautogui takes as a
# PIL(pillow) and in RGB we need to
# convert it to numpy array and BGR
# to write it to disk
#image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

#cv2.imwrite("image2.png", image)

#hash0 = imagehash.average_hash(Image.open('image1.png'))
#hash1 = imagehash.average_hash(Image.open('image2.png'))
#cutoff = 5  # maximum bits that could be different between the hashes

#if hash0 - hash1 < cutoff:
#  print('images are similar')
#else:
#  print('images are not similar')
def main():
    print("What would you like to do?")
    print("1 - Take Base Screenshot")
    print("2 - Run Program")
    action = input()

    if action == "1":
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite("image1.png", image)
        print("screenshot success")
        main()

    if action == "2":
        autoClose()

    if action != "1" or "2":
        print ("That Feature isn't implemented yet!")
        main()

def autoClose():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("image2.png", image)
    print("compare success")
    hash0 = imagehash.average_hash(Image.open('image1.png'))
    hash1 = imagehash.average_hash(Image.open('image2.png'))
    cutoff = 5  # maximum bits that could be different between the hashes

    if hash0 - hash1 < cutoff:
        print('images are similar')
        closeWindow()
    else:
        print('images are not similar')

    time.sleep(3)
    autoClose()

def closeWindow():
    # move the mouse and do whatever you want to
    print("the mouse is doin something")


main()
input()