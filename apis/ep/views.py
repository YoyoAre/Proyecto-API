from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    response = requests.get('http://localhost:8080/usuario').json()
    return render(request,'home.html',{'response':response})

def agregar(request,nombre):
    name = {'nombre':nombre}
    response = requests.post('http://localhost:8080/usuario',json=name).json()
    return render(request,'agregar.html',{'response':response})

def actualiza(request,id,nombre):
    name = {'id':id,'nombre':nombre}
    response = requests.post('http://localhost:8080/usuario',json=name).json()
    return render(request,'actualiza.html',{'response':response})
