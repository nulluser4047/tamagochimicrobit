import serial
import pygame
from pathlib import Path

# Inicializar el sistema de audio
pygame.mixer.init()

# Cargar el audio antes de detectar movimientos
audio_file = Path(__file__).parent / "argentina.mp3"
voice = pygame.mixer.Sound(str(audio_file))

# Conectar con la micro:bit
connection = serial.Serial("COM12", 115200, timeout=1)

print("Waiting for the micro:bit...")

while True:
    # Recibir el mensaje de la placa
    message = connection.readline().decode("utf-8").strip()

    # Reproducir la voz al detectar movimiento
    if message == "SHAKE":
        print("Shake detected!")
        voice.stop()
        voice.play()
