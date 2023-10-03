from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
# home
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('reset/<str:email>/', views.reset, name='reset'),
    path('verifyemail', views.verifyemail, name='verifyemail'),
    path('register', views.register, name='register'),
    path('otp', views.otp_verify, name='otp'),
# user
    path('profile', views.profile, name='profile'),
# complaines
    path('complaint', views.complaint, name='complaint'),
    path('complaintfrom', views.complaintfrom, name='complaintfrom'),
# other
    path('schemes', views.schemes, name='schemes'),
    path('notice', views.notice, name='notice'),
    path('bugets', views.bugets, name='bugets'),
# appointment
    path('appointment', views.appointment, name='appointment'),
    path('appointmentfrom', views.appointmentfrom, name='appointmentfrom'),
# logout
    path('logout', views.logout, name='logout'),
]