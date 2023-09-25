from microbit import *
import radio
import music

radio.on()
radio.config(channel=9)

state = "waiting"


while True:
    POT = pin1.read_analog()
    if state == "waiting":
        display.clear()
        message = radio.receive()
        if message == "twist it":
            music.play(music.DADADADUM, wait=False)
            state = "received"
    if state == "received":
        start = running_time()
        display.show(Image.DIAMOND)
        state = "playing"
    if state == "playing":
        if POT < 5 or POT > 1015:
            end = running_time()
            music.play(music.BA_DING)
            state = "checking"
    if state == "checking":
        time = end - start
        if time > 3000:
            state = "incomplete"
        if time < 3000:
            state = "completed"
    if state == "completed":
        radio.send("completed")
        state = "waiting"
    if state == "incomplete":
        radio.send("incomplete")
        state = "waiting"

