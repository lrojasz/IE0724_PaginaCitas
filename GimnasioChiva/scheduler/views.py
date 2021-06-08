from django.shortcuts import render, redirect

# Página principal
def index(request):
    return render(request,'index.html',{})

# Redirigir página de home
def home(request):
    return redirect('home/')

# Página de "contactarnos"
def login(request,login='false'):
    login = 'false'
    if request.method == "POST":
        #do stuff
        user = request.POST['user']
        password = request.POST['password']
        login = 'true'
        # pass in variables
        return render(request,'login.html',{'login':login})
    else:
        return render(request,'login.html',{'login':login})

# Página de nueva cita
def schedule(request):
    return render(request,'schedule.html',{})

# Página de about_us
def about_us(request):
    return render(request,'about-us.html',{})

# Página de galeria
def gallery(request):
    return render(request,'gallery.html',{})


    