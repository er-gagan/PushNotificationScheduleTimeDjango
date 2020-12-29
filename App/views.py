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

    # data = request.user.objects.all()
    time1 = "17:58"
    time2 = "18:00"
    Notify.delay(time1,time2)
    time1 = "17:59"
    time2 = "18:01"
    Notify.delay(time1,time2)
    return redirect('/')