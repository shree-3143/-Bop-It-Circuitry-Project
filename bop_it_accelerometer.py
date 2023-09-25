from microbit import *
import radio
import random
import music

radio.on()
radio.config(channel = 9)
state = "waiting"

while True:
    if state == "waiting":
        display.clear()
        message = radio.receive()
        if message == "shake it":
            music.play(music.BADDY, wait=False)
            state = "received"
    elif state == "received":
        start = running_time()
        display.show(Image.SQUARE)
        state = "playing"
    elif state == "playing":
        time = running_time() - start
        if time > 3000:
            state = "incomplete"
        if accelerometer.was_gesture("shake"):
            state = "completed"
    elif state == "completed":
        music.play(music.BA_DING)
        radio.send("completed")
        state = "waiting"
    elif state == "incomplete":
        radio.send("incomplete")
        music.play(music.WAWAWAWAA)
        state = "waiting"
