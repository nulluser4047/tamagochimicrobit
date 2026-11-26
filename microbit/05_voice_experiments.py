from microbit import *
import speech

# Comparamos seis voces con la misma frase.
voices = [
    {},
    {"pitch": 35, "speed": 80, "mouth": 140, "throat": 100},
    {"pitch": 45, "speed": 92, "mouth": 190, "throat": 190},
    {"pitch": 85, "speed": 85, "mouth": 105, "throat": 110},
    {"pitch": 25, "speed": 65, "mouth": 160, "throat": 110},
    {"pitch": 100, "speed": 120, "mouth": 200, "throat": 100}
]

for i, voice in enumerate(voices):
    display.show(str(i + 1))  # Número de voz
    speech.say("Hello, human!", **voice)  # Aplica los parámetros
    sleep(2000)

display.show(Image.HAPPY)
