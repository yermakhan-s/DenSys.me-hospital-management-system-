from django.urls import path
from . import views

app_name='hospitalapp'
urlpatterns=[
    path("login/", views.log_in_view, name="login"),
    path("appointment/", views.appointment, name="appointment"),
    path("create_appointment/<int:id>/", views.create_appointment, name="create_appointment"),
    path("make_appointment/<str:id>/", views.make_appointment, name="make_appointment")
]