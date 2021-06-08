from django.shortcuts import render

# Página principal
def index(request):
    return render(request,'index.html',{})

# Página de "contactarnos"
def login(request):
    return render(request,'login.html',{})

# Página de nueva cita
def schedule(request):
    return render(request,'schedule.html',{})

    