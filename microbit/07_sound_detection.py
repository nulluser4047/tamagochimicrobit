# Requiere micro:bit V2 con micrófono.
from microbit import *
import speech
import random

answers = ["Hello, human!", "I am listening", "Tell me more", "Really?", "I like you"]
display.show(Image.HAPPY)

while True:
    if microphone.was_event(SoundEvent.LOUD):  # Detecta volumen, no palabras
        display.show(Image.SURPRISED)
        speech.say(random.choice(answers), pitch=35, speed=80, mouth=140, throat=100)
        display.show(Image.HAPPY)
        sleep(1500)
        microphone.was_event(SoundEvent.LOUD)  # Descarta un posible eco propio
    sleep(100)
