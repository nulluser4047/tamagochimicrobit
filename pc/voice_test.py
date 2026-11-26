# Este código se ejecuta en Windows, no en la micro:bit.
import pyttsx3

engine = pyttsx3.init()  # Inicia el sintetizador de voz
voices = engine.getProperty("voices")  # Obtiene las voces instaladas

for i, voice in enumerate(voices):
    print(i, voice.name)  # Muestra el número y nombre
    engine.setProperty("voice", voice.id)  # Selecciona la voz
    engine.setProperty("rate", 155)  # Velocidad
    engine.say("Hello, human! I am your little robot.")
    engine.runAndWait()  # Reproduce la frase antes de continuar
