import schedule
import time
import json
import datetime
import playsound
mp3_files = ["1.mp3","2.mp3"]
yet = []
def job():
    global yet
    f = open('times.json','r')
    # работа с фа
    json_string = ''.join(f.readlines())
    data = json.loads(json_string)
    now = datetime.datetime.now()

    if(yet != [[now.hour,now.minute]]):
        yet = []
    first = [a for a in data if a[0][0] == now.hour and a[0][1] == now.minute and a[0] not in yet]
    #for a in data:
    #    print(a,a[1],a[1][0] == now.hour, a[1][1] == now.minute , a[1] not in yet )
    second = [a for a in data if a[1][0] == now.hour and a[1][1] == now.minute and a[1] not in yet ]
    f.close()

    print(yet,first,second)        

    if(first != []):
        yet.append(first[0][0])
        print("append first ",first[0][0])
        print("Звенит звонок на урок")
        playsound.playsound(mp3_files[0], True)
    if(second != []):
        yet.append(second[0][1])
        print("append second ", second[0][1])
        print("Звенит звонок с урока")
        playsound.playsound(mp3_files[1], True)
    print(yet,first,second)        
schedule.every(5).seconds.do(job)
# нужно иметь свой цикл для запуска планировщика с периодом в 1 секунду:
while True:
    schedule.run_pending()
    time.sleep(1)