from django.shortcuts import redirect, render
import schedule
import time
from datetime import date
import requests
import json

# Create your views here.
def home(request):
    return render(request,'App/home.html')

def notification(request):
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

    start_date = date(2020, 12, 28)
    end_date = date(2020, 12, 28)
    delta = end_date - start_date
    Days = delta.days+1

    time1 = "17:14"
    time2 = "17:15"

    for count in range(1,Days+1):
        count-=1
        schedule.every().monday.at(time1).do(job, count=count, Days=Days)
        count+=1
        schedule.every().monday.at(time2).do(job, count=count, Days=Days)
        
    while 1:
        schedule.run_pending()
        time.sleep(1)
    return redirect('/')