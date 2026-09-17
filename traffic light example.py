state = "green"

if state == "green":
    print("GREEN LIGHT")
elif state == "yellow":
    print("YELLOW LIGHT")
elif state == "red":
    print("RED LIGHT")

while True:
    if state == "green":
        print("GREEN LIGHT")
    elif state == "yellow":
        print("YELLOW LIGHT")
    elif state == "red":
        print("RED LIGHT")

import time
state = "green"
while True:
    if state == "green":
        print("GREEN LIGHT")
        time.sleep(5)
        state = "yellow"
    elif state == "yellow":
        print("YELLOW LIGHT")
        time.sleep(1)
        state = "red"
    elif state == "red":
        time.sleep(5)
        print("RED LIGHT")
        state = "green"

        "uh this one failed really badly ill see if i can fix it, but both the extension and main.py docs are completed without any problems."