from django.shortcuts import redirect, render
import schedule
import time
from datetime import date
import requests
import json
from .task import Notify
# Create your views here.
def home(request):
    return render(request,'App/home.html')

def notification(request):
    Time1 = request.GET['time1']
    Time2 = request.GET['time2']
    Time3 = request.GET['time3']
    Time4 = request.GET['time4']

    Day1 = request.GET['day1']
    Month1 = request.GET['month1']
    Year1 = request.GET['year1']
    Day2 = request.GET['day2']
    Month2 = request.GET['month2']
    Year2 = request.GET['year2']

    # print(Time1,Time2,Time3,Time4,Day1,Month1,Year1,Day2,Month2,Year2)
    time1 = Time1
    time2 = Time3
    Notify.delay(time1,time2,Day1,Month1,Year1,Day2,Month2,Year2)
    time1 = Time2
    time2 = Time4
    Notify.delay(time1,time2,Day1,Month1,Year1,Day2,Month2,Year2)
    return redirect('/')