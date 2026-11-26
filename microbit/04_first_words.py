from microbit import *
import speech  # Sintetizador de voz

display.show(Image.ASLEEP)  # El robot duerme
sleep(2000)
display.show(Image.SURPRISED)  # Se despierta
speech.say("System activated")
sleep(1000)
display.show(Image.HAPPY)
speech.say("Hello, human!")
sleep(1000)
speech.say("I am alive!")
display.show(Image.HEART)
