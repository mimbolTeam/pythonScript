"""
Auto calls
"""
import datetime
import json
import time

import playsound

mp3_files = ["1.mp3", "2.mp3"]
auto_timer = []
DEV_MODE = False
JSON_NAME = 'times.json' if not DEV_MODE else 'times.dev.json'

while True:
    with open(JSON_NAME, 'r', encoding='utf8') as temp_file:
        json_string = temp_file.read()

    data = json.loads(json_string)
    now = datetime.datetime.now()

    if auto_timer != [now.hour, now.minute]:
        auto_timer = []
    first = [a for a in (data[datetime.datetime.today().weekday()] if not DEV_MODE else data)
             if a[0][0] == now.hour and a[0] [1] == now.minute and a[0] != auto_timer]
    second = [a for a in (data[datetime.datetime.today().weekday()] if not DEV_MODE else data)
             if a[1][0] == now.hour and a[1] [1] == now.minute and a[1] != auto_timer]
    if first:
        auto_timer = first[0][0]
        print("Звенит звонок на урок")
        playsound.playsound(mp3_files[0], True)
    if second:
        auto_timer = second[0][1]
        print("Звенит звонок с урока")
        playsound.playsound(mp3_files[1], True)

    time.sleep(1)
    
