from django.shortcuts import redirect, render
from .task import Notify
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'App/home.html')

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

    UserId = request.GET['user_id']
    if UserId:
        time1 = Time1
        time2 = Time3
        Notify.delay(UserId,time1,time2,Day1,Month1,Year1,Day2,Month2,Year2)
        time1 = Time2
        time2 = Time4
        Notify.delay(UserId,time1,time2,Day1,Month1,Year1,Day2,Month2,Year2)
    return redirect('/')