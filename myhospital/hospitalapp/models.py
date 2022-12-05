import datetime

from django.db import models

class Patient(models.Model):
    birth_date=models.CharField(max_length=30)
    IIN=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    middlename=models.CharField(max_length=30)
    bloodgroup=models.CharField(max_length=30)
    emergencycontactnumber=models.CharField(max_length=30)
    contactnumber=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    addres=models.CharField(max_length=30)
    maritalstatus=models.CharField(max_length=30)
    registrationdate=models.CharField(max_length=30)
    optionaldetails=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Doctor(models.Model):
    birth_date = models.CharField(max_length=30)
    IIN = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    bloodgroup = models.CharField(max_length=30)
    emergencycontactnumber = models.CharField(max_length=30)
    contactnumber = models.CharField(max_length=30)
    departmentID=models.CharField(max_length=30)
    specaliztionID=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='images/')
    addres = models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    priceoftheappointment=models.CharField(max_length=30)
    scheduledetails=models.CharField(max_length=30)
    degree=models.CharField(max_length=30)
    rating=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name} {self.surname} {self.specaliztionID}"

class Appointment(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date = models.DateField(default=datetime.date.today)
    specalization=models.CharField(max_length=30)
    doctor =models.ForeignKey(Doctor, on_delete=models.CASCADE)
    contacts = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default="Pending...")
    def __str__(self):
        return f"{self.doctor}"


