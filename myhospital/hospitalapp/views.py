from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from .models import *

from django.contrib.auth.models import User, Group
# Create your views here.
def log_in_view(request):
    return render(request,"login.html")

def appointment(request):
    doctor = Doctor.objects.order_by().values('specaliztionID').distinct()


    return render(request, "appointment.html", {"doctor": doctor})
def create_appointment(request,id):
    if request.method == "POST":
        doc=Doctor.objects.all()
        appointment = Appointment()
        appointment.name = request.POST.get("name")
        appointment.surname = request.POST.get("surname")
        appointment.doctor = doc[id]
        appointment.date = request.POST.get("date")
        appointment.specalization = request.POST.get("spec")
        appointment.contacts = request.POST.get("contacts")
        appointment.save()
        return HttpResponse("APPOINTMENT REQUEST SUBMITTED SUCCESSFULLY")
    else:
        return render(request,"create_appointment.html", {"pk":id})

def make_appointment(request, id):

    doctor = Doctor.objects.filter(specaliztionID=id).all()
    return render(request, "make_appointment.html", {"doc": doctor})
