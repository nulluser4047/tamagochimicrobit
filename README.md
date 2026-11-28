# Tamagotchi Microbit

## Español
Proyecto personal de práctica y desarrollo con Python, MicroPython y robótica con BBC micro:bit. El objetivo es construir una mascota virtual con personalidad, emociones, voz y, más adelante, reconocimiento de voz e inteligencia artificial.

En este repositorio se publicarán únicamente los programas que haya probado y decidido guardar. Los experimentos de la placa se realizan en el [editor oficial de Python](https://python.microbit.org/).

## English
A personal Python, MicroPython and robotics practice and development project using BBC micro:bit. The goal is to build a virtual pet with personality, emotions and speech, eventually adding voice recognition and AI. Only tested and approved programs will be published here.

## Русский
Личный практический проект по разработке с использованием Python, MicroPython и робототехники с BBC micro:bit. Цель — создать виртуального питомца с характером, эмоциями и голосом, а затем добавить распознавание речи и искусственный интеллект. Здесь будут публиковаться только проверенные и одобренные программы.

## Archivos / Files / Файлы

- [python/](python/): código fuente editable / editable source code / исходный код.
- [hex/](hex/) (archivos para transferir directamente a la micro:bit por USB) / ready-to-flash files / файлы для загрузки на плату.

### 01 — My First Baby Words

El robot despierta, bosteza, saluda, pide que lo agiten, muestra una cara divertida, se despide y vuelve a dormir. Código Python probado y aprobado; [archivo HEX disponible](hex/1.myfirtsbabywords.hex).


### 02 — Angry Tamagotchi / Tamagotchi enojado / Сердитый тамагочи

**ES:** La micro:bit comienza con una cara feliz. Al agitarla muestra una cara de enojo que permanece hasta reiniciar la placa y envía `SHAKE` por USB. El programa de Windows recibe el mensaje y reproduce una frase rioplatense precargada mediante Pygame, sin abrir un reproductor externo. Prueba física aprobada el 28/11/2026; respuesta percibida como inmediata, sin medición instrumental.

**EN:** The micro:bit starts with a happy face. Shaking it displays a persistent angry face until reset and sends `SHAKE` over USB. The Windows program receives the event and plays a preloaded Rioplatense Spanish voice clip through Pygame, without launching an external player. Physical test passed on 28 November 2026; perceived immediate response, not benchmarked.

**RU:** При запуске micro:bit показывает счастливое лицо. При встряхивании появляется сердитое лицо, которое сохраняется до перезапуска платы, а по USB отправляется сообщение `SHAKE`. Программа Windows воспроизводит заранее загруженную реплику на испанском языке с помощью Pygame без внешнего проигрывателя. Проверено 28.11.2026; отклик воспринимается как мгновенный, точные измерения не проводились.

- [MicroPython — 02_angry_tamagotchi.py](python/02_angry_tamagotchi.py)
- [Windows Python — voice_bridge.py](python/voice_bridge.py)
- [HEX](hex/): carpeta de archivos para la placa / firmware files / файлы для платы.

#### Uso / Usage / Использование

1. Cargar el programa MicroPython en la placa desde el editor oficial, o transferir su HEX cuando esté disponible. / Flash the MicroPython program or its HEX when available. / Загрузите программу MicroPython или её HEX-файл, когда он будет доступен.
2. Conectar la micro:bit por USB a Windows. Instalar las dependencias y comprobar el puerto serie. / Connect the board to Windows via USB, install dependencies and check the serial port. / Подключите плату к Windows по USB, установите зависимости и проверьте последовательный порт.

```powershell
python -m pip install pyserial pygame edge-tts
python -m serial.tools.list_ports
```

3. En la carpeta que contiene `voice_bridge.py`, generar el MP3 de prueba (requiere internet). / In the directory containing `voice_bridge.py`, generate the test MP3 (internet required). / В папке с `voice_bridge.py` создайте тестовый MP3 (нужен интернет).

```powershell
python -m edge_tts --voice es-AR-TomasNeural --pitch=+35Hz --rate=+15% --text "Bo, ¿qué carajo hacés? Dejá de sacudirme, animal." --write-media argentina.mp3
```

4. Cambiar `COM12` en el código si Windows asigna otro puerto; cerrar cualquier monitor serial antes de ejecutar. / Change `COM12` if necessary; close any serial monitor before running. / При необходимости замените `COM12` и закройте монитор последовательного порта.

```powershell
python voice_bridge.py
```

**ES:** El MP3 no se incluye en el repositorio. Se genera una vez y se reproduce desde la memoria. La voz sale por los parlantes de la computadora; esta versión todavía no integra el modo autónomo ni genera frases nuevas durante la interacción.

**EN:** The MP3 is not included; generate it once and play it from memory. Audio comes from the PC speakers. Autonomous fallback and dynamic speech generation are not yet integrated.

**RU:** MP3 не включён в репозиторий: создайте его один раз, затем звук воспроизводится из памяти. Звук идёт через динамики компьютера. Автономный режим и динамический синтез речи пока не интегрированы.
