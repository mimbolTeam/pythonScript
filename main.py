"""
Provides import basic and custom modules
"""
import datetime
import json
import time

import playsound
import schedule

mp3_files = ["1.mp3", "2.mp3"]
YET = []


def job():
    """
Provides reading date from file times.json and writing to the end of the file
    """
    with open('times.json', 'r', encoding='utf8') as temp_file:
        contents = temp_file.read()
    json_string = ''.join(contents.readlines())
    data = json.loads(json_string)
    now = datetime.datetime.now()
    if YET != [[now.hour, now.minute]]:
        YET = []
        first = [a for a in data if a[0][0] == now.hour and a[0]
                 [1] == now.minute and a[0] not in YET]
        second = [a for a in data if a[1][0] == now.hour and a[1]
                  [1] == now.minute and a[1] not in YET]

        print(YET, first, second)

    if first:
        YET.append(first[0][0])
        print("append first", first[0][0])
        print("Звенит звонок на урок")
        playsound.playsound(mp3_files[0], True)
    if second:
        YET.append(second[0][1])
        print("append second ", second[0][1])
        print("Звенит звонок с урока")
        playsound.playsound(mp3_files[1], True)
    print(YET, first, second)
    schedule.every(5).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
