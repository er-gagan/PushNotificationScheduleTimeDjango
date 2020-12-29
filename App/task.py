from celery import shared_task
import schedule
import time
from datetime import date
import requests
import json

@shared_task
def Notify():
    def push():
        header = {"Content-Type": "application/json; charset=utf-8",
            "Authorization": "Basic MDQwMzgzYTgtNDM5My00YTQwLWI0MTUtNTI0ZWViOTkzZWRm"}

        payload = {"app_id": "b7a3f46c-d540-43d9-9b4c-fc3b31a95b83",
            "included_segments": ["Subscribed Users"],
            "headings": {"en": "Congratulations!!!"},
            "contents": {"en": "This is push notification"}
            }

        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        # print(req.status_code, req.reason)

    def job(count,Days):
        if count == Days:
            push()
            exit(0)
        else:
            push()

    start_date = date(2020, 12, 29)
    end_date = date(2020, 12, 29)
    delta = end_date - start_date
    Days = delta.days+1

    time1 = "10:12"
    time2 = "10:13"

    for count in range(1,Days+1):
        count-=1
        schedule.every().tuesday.at(time1).do(job, count=count, Days=Days)
        count+=1
        schedule.every().tuesday.at(time2).do(job, count=count, Days=Days)
        
    while 1:
        schedule.run_pending()
        time.sleep(1)