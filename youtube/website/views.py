from django.shortcuts import render
from website.models import Mylogin

# Create your views here.
def index(request):
    return render(request , 'index.html')

def login1(request):
    if request.method =='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        login = Mylogin(name=name , password= password , email=email)
        login.save()
    return render(request , 'login.html')

def codes1(request):
    return render(request , 'codes.html')