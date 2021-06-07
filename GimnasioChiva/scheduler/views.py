from django.shortcuts import render

# Página principal
def index(request):
    return render(request,'index.html',{})

# Página de "contactarnos"
def contact(request):
    return render(request,'contact.html',{})