import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
position1 = pt.locateOnScreen("C:\\Users\\ASUS\\PycharmProjects\\whatsapp-chatbot\\whatsapp\\emoji_and_paperclip.png")
x = position1[0]
y = position1[1]


# gets message
def get_message():
    global x, y

    position = pt.locateOnScreen(
        "C:\\Users\\ASUS\\PycharmProjects\\whatsapp-chatbot\\whatsapp\\emoji_and_paperclip.png")
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=0.5)
    pt.moveTo(x + 60, y - 80, duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(40, -300)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print(f"Message received :{whatsapp_message}")

    return whatsapp_message


# post
def post_response(message):
    global x, y

    position = pt.locateOnScreen(
        "C:\\Users\\ASUS\\PycharmProjects\\whatsapp-chatbot\\whatsapp\\emoji_and_paperclip.png")
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 30)
    pt.click()
    pt.typewrite(message)


post_response(get_message())
