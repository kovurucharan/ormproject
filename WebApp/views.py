from django.shortcuts import render
from WebApp.models import State

def Stateview(request):
    items=State.objects.all()
    return render(request,'MyApp/Welcome.html',{'items':items})
