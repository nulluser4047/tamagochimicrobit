from microbit import *
import music  # Importa melodías

while True:
    if button_a.was_pressed():
        music.play(music.POWER_UP)  # Sonido de encendido
    if button_b.was_pressed():
        music.play(music.POWER_DOWN)  # Sonido de apagado
    sleep(20)
