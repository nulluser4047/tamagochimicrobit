# Versión inicial: primeras palabras con la voz 2.
# Cargar este archivo en la micro:bit mediante el editor oficial.
from microbit import *
import speech

def say(text):
    speech.say(text, pitch=35, speed=80, mouth=140, throat=100)

display.show(Image.ASLEEP)
sleep(2000)
display.show(Image.SURPRISED)
say("System activated")
sleep(1000)
display.show(Image.HAPPY)
say("Hello, human!")
sleep(1000)
say("I am alive!")
display.show(Image.HEART)
