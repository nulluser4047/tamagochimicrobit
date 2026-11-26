# Tamagotchi Microbit

## Español
Proyecto personal de aprendizaje de Python, MicroPython y robótica con una BBC micro:bit de Ceibal (probablemente V2, por confirmar). La idea es crear una mascota virtual que tenga expresiones, personalidad, emociones y voz, y eventualmente pueda conversar mediante una computadora.

### Cómo probar los programas
1. Abrir un archivo de la carpeta `microbit`.
2. Copiar su código al [editor oficial](https://python.microbit.org/).
3. Descargar el archivo HEX y copiarlo a la unidad MICROBIT por USB. No renombrar un archivo PY a HEX.
4. Para los programas de `pc`, abrir una terminal en VS Code e instalar las dependencias con `python -m pip install -r requirements.txt`.
5. Ejecutar `python pc/voice_test.py` desde la raíz del repositorio.

Cada experimento de la placa se carga por separado. Los programas de PC no se cargan en la micro:bit. La voz de PC sale por sus parlantes.

### Registro
- [x] Primeras palabras: probado por la autora en su placa.
- [x] Selección de voz 2: preferida por la autora.
- [ ] Probar personalidad y detección de sonido.
- [ ] Probar voces de Windows.
- [ ] Comunicación USB y cambio automático de voz.
- [ ] Hambre, energía, felicidad y sueño.
- [ ] Reconocimiento de voz e inteligencia artificial.

Los demás ejemplos se conservan como experimentos pendientes de validación física. El programa principal inicial usa la voz 2; aún no es un Tamagotchi completo.

## English
A personal learning project using Python, MicroPython and a BBC micro:bit to build a virtual pet with expressions, personality and speech. Board scripts are in `microbit/`; desktop scripts are in `pc/`. Flash each board experiment separately using the official Python editor. Install desktop dependencies using `python -m pip install -r requirements.txt`. Natural PC speech, USB communication, voice recognition and AI are planned, not yet integrated.

## Русский
Учебный проект по Python, MicroPython и робототехнике с BBC micro:bit. Цель — создать виртуального питомца с эмоциями, характером и голосом. Программы для платы находятся в папке `microbit/`, программы для компьютера — в `pc/`. Каждый эксперимент для платы загружается отдельно через официальный редактор Python. Связь с компьютером, распознавание речи и искусственный интеллект пока в планах.
