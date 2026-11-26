from microbit import *  # Importa las funciones de la placa

while True:  # Repite el programa indefinidamente
    if button_a.was_pressed():  # Detecta el botón A
        display.show(Image.HEART)  # Muestra un corazón
        sleep(1000)  # Espera un segundo
        display.clear()  # Apaga los LED
