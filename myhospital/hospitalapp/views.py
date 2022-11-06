from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
# Create your views here.
def log_in_view(request):

    return render(request,"login.html")