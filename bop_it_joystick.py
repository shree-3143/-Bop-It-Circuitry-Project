# Write your code here :-)
from microbit import *
import music
import radio
radio.on()

X = pin1
Y = pin2

radio.config(channel = 9)
state = "waiting"
while True:
    x = X.read_analog()
    y = Y.read_analog()
    if state == "waiting":
        display.clear()
        msg = radio.receive()
        if msg == "pull it":
            music.play(music.CHASE, wait = False)
            display.show(Image.ARROW_N)
            state = "received"
    elif state == "received":
        start = running_time()
        state = "playing"
    elif state == "playing":
        time = running_time() - start
        if time > 3000:
            state = "incomplete"
        if y > 900:
            state = "correct"
        if x > 900:
            state = "correct"
        if y < 100:
            state = "correct"
        if x < 100:
            state = "correct"
    elif state == "correct":
        radio.send("completed")
        music.play(music.BA_DING)
        state = "waiting"
    elif state == "incorrect":
        radio.send("incomplete")
        state = "waiting"# Write your code here :-)
