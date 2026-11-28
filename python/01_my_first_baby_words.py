from microbit import *
import speech

# Configuración de la voz 2
def say(text):
    speech.say(text, pitch=35, speed=80,
               mouth=140, throat=100)


# Cara bostezando
yawn = Image("00000:"
             "99099:"
             "00000:"
             "09990:"
             "09990:")


# Cara de risa con los ojos cerrados
laugh = Image("90009:"
              "09090:"
              "90009:"
              "09990:"
              "00900:")


# 1. El robot está dormido
display.show(Image.ASLEEP)
sleep(3000)


# 2. Se despierta bostezando
display.show(yawn)
say("Yaaaawn")
sleep(1000)


# 3. Nos saluda
display.show(Image.HAPPY)
display.scroll("HELLO HUMAN", delay=120)
say("Hello human")
sleep(1000)


# 4. Nos pide que lo agitemos
say("Shake me")
display.scroll("SHAKE ME", delay=120)

# Descartamos movimientos anteriores
accelerometer.was_gesture("shake")

# Espera hasta que lo agitemos
while not accelerometer.was_gesture("shake"):
    sleep(50)


# 5. Muestra una cara divertida sin sonido
display.show(laugh)
sleep(2000)


# 6. Se despide
display.show(Image.HAPPY)
say("Bye bye silly")
display.scroll("BYE BYE SILLY", delay=120)


# 7. Vuelve a dormirse
display.show(yawn)
say("Yaaaawn")
sleep(1000)

display.show(Image.ASLEEP)

# Permanece dormido
while True:
    sleep(1000)

# @404_nulluser
