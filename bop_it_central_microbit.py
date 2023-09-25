from microbit import *
import radio
import random
import music
radio.on()

radio.config(channel=9)
state = "waiting"
TASKS  = ["bop it", "shake it", "twist it", "pull it"]

while True:
    if state == "waiting":
        i = 0
        display.show(Image.HAPPY)
        if button_a.was_pressed():
            state = "random action"
            task = random.choice(TASKS)
            radio.send(task)
    if state == "playing":
        display.show(Image.HAPPY)
        state = "random action"
        task = random.choice(TASKS)
        radio.send(task)
    if state == "random action":
        message = radio.receive()
        if message == "completed":
            display.show(Image.BUTTERFLY)
            music.play(music.RINGTONE)
            state = "playing"
            i += 1
        if message == "incomplete":
            display.show(Image.SKULL)
            music.play(music.WAWAWAWAA)
            display.scroll("Score:" + str(i))
            state = "waiting"



