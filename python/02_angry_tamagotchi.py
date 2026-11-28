from microbit import *

# Comienza con cara feliz
display.show(Image.HAPPY)

while True:
    # Detectar si lo sacuden
    if accelerometer.was_gesture("shake"):
        display.show(Image.ANGRY)
        print("SHAKE")
        sleep(2000)

    sleep(50)
