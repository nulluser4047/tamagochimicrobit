from microbit import *
import speech

def say(text):
    # Usamos la voz 2, elegida en el experimento anterior.
    speech.say(text, pitch=35, speed=80, mouth=140, throat=100)

say("System activated")
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        display.show(Image.HEART)
        say("I love you")
    if button_b.was_pressed():
        display.show(Image.ANGRY)
        say("Do not touch me")
    if accelerometer.was_gesture("shake"):
        display.show(Image.SAD)
        say("Stop shaking me")
    sleep(100)
