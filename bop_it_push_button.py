from microbit import *
import radio
import music

radio.on()
radio.config(channel=9)

state = "waiting"
BUTTON = pin1
BUTTON.set_pull(BUTTON.PULL_UP)

while True:
    if state == "waiting":
        display.clear()
        message = radio.receive()
        if message == "bop it":
            music.play(music.BLUES, wait=False)
            state = "received"
    elif state == "received":
        start = running_time()
        display.show(Image.TRIANGLE)
        state = "playing"
    elif state == "playing":
        time = running_time() - start
        if time > 3000:
            state = "incomplete"
        if BUTTON.read_digital() == 0:
            state = "completed"
    elif state == "completed":
        music.play(music.BA_DING)
        radio.send("completed")
        state = "waiting"
    elif state == "incomplete":
        music.play(music.WAWAWAWAA)
        radio.send("incomplete")
        state = "waiting"
