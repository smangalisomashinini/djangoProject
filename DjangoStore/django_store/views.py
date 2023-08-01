from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    return render(request,'index.html')
def userReg(request):
    return render(request,'userReg.html')

def insertuser(request):
    vuid = request.POST['tuid']
    vuname = request.POST['tuname']
    vuemail = request.POST['tuemail']
    vucontact = request.POST['tucontact']

    us = User(uid = vuid, uname = vuname, uemail = vuemail, ucontact = vucontact)
    us.save()

    return render(request, 'index.html')

