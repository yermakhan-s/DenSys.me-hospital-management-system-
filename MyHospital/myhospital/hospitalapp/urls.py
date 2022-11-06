from django.urls import path
from . import views

app_name='hospitalapp'
urlpatterns=[
    path("login/", views.log_in_view, name="login")
]