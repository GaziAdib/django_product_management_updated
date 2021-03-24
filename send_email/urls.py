from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_my_mail, name='sendEmail')
]