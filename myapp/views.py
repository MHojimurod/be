from django.shortcuts import redirect, render
from .models import Qabul
# Create your views here.
def home(request):
    return render(request,'be/index.html')


def qabul(request,**kwargs):
    data = request.GET
    data.get('name')
    data.get('surname')
    data.get('phone')
    data.get('email')
    data.get('date')
    data.get('time')
    data.get('msg')
    print(data,"aa")
    if data:
        Qabul.objects.create(name=data.get('name'), email=data.get('email'),surname=data.get('surname'),phone=data.get('phone'),date=data.get('date'),time=data.get('time'),msg=data.get('msg'))
        return redirect("home")
    return render(request,'be/qabul.html')
