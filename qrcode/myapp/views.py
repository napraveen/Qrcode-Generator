from django.shortcuts import render,redirect

from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import data


def generateData(request):
    if request.method=="POST":
        post=data.objects.all()[0]
        post.data=request.POST['data']
        post.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
def qrcode(request):
    qrobj = data.objects.all()
    return render(request,'qr.html',{'qr':qrobj})