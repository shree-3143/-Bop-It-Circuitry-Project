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
        time = running_time() - start
        if time > 3000:
            state = "incomplete"
        if POT < 5 or POT > 1015:
            state = "completed"
    if state == "completed":
        music.play(music.BA_DING)
        radio.send("completed")
        state = "waiting"
    if state == "incomplete":
        music.play(music.WAWAWAWAA)
        radio.send("incomplete")
        state = "waiting"
