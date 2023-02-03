from django.urls import path 
from . import views

urlpatterns=[
    path('', views.generateData, name="generatedata"),
    path('qr',views.qrcode,name ="code"),
]