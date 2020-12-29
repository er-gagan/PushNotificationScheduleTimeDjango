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
    data = request.user.objects.all()
    Notify.delay()
    return redirect('/')