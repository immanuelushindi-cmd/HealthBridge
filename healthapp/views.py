from django.shortcuts import render
from healthapp.models import*

# Create your views here.
def home(request):
    return render(request, 'index.html')
def starter(request):
    return render(request, 'starter-page.html')
def about(request):
    return render(request, 'about.html')

def appointment(request):
    if request.method == 'POST':
        Myappointment.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            datetime=request.POST.get('datetime'),
            department=request.POST.get('department'),
            doctor=request.POST.get('doctor'),
            message=request.POST.get('message')
        )

        return render(request, 'appointment.html')
    else:
        return render(request, 'appointment.html')

def show(request):
    allappointment = Myappointment.objects.all()
    return render(request,'show.html',{'allappointment': allappointment})


