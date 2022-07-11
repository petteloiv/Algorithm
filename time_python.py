import schedule
import time
import datetime

# datetime.datetime.now()

def ttime():
    print(datetime.datetime.now())

schedule.every(1).minutes.do(ttime)


while True:
    schedule.run_pending()
    time.sleep(1)