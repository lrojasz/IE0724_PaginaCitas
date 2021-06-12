from django.contrib.auth.models import User
from appointments.models import Appointments
from django.shortcuts import render
from django.views.generic.list import ListView #Importando la vista como lista
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView #Crear un appointment y modificar un appointment.
from django.urls import reverse_lazy #Se devuelve a algún lado despues de crear

#TENEMOS AUTENTICATION VIEWS
from django.contrib.auth.views import LoginView #Importamos login

from django.contrib.auth.mixins import LoginRequiredMixin #El tipo de usuario

from django.contrib.auth.forms import UserCreationForm #Crear un user

from django.contrib.auth import login #Apenas se registra llevarlo a login

from .models import Appointments

class CustomLoginView(LoginView):
    #Nos va a redirigir a un template
    template_name = 'appointments/login.html'
    #Nos va a dar un form y le decimos que todos, ese form se envía al template
    fields = '__all__'
    #Previene a un user a estar en esta página
    redirect_authenticated_user = True
    #Una vez que se hace sign in, se va a ir a una página
    def get_success_url(self): 
        return reverse_lazy('appointments') #Vamos a mandarlo al appointments(Ver las citas)

#LOGINREQUIREDMIXIN NOS VA A SIEMPRE REDIRECCIONAR A LOGIN SI NO SE ESTÁ LOGEADO

class RegisterPage(FormView): #Vamos a traer el form view
    #Lo enviamos a este template
    template_name = 'appointments/register.html'
    form_class = UserCreationForm # Con este form vamos a crear el user(User creation form)
    redirect_authenticated_user = True #Users authenticated se van a redirigir
    #Apenas haya success se va a mandar a ver las citas
    success_url = reverse_lazy('appointments')
    # Vamos a redireccionar el user
    def form_valid(self, form): #Le estamos pasando el form
        user = form.save() # Va a retornar el user ya que es el User Create form
        if user is not None: #Si el usuario es válido  
            login(self.request, user) #Ir al login con esta función, autenticandolo, pasandole el request y el use
        return super(RegisterPage, self).form_valid(form)
    
    # def get(self, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)


#Primer parámetro le está diciendo al view que restrinja esa vista de todos los appointments
class AppointmentsList(LoginRequiredMixin, ListView): #Será una clase y tenemos la funcionalidad de ListView
    model = Appointments #Toma el modelo Appointments
    # El view busca por el template appointments_list.html, como la ve ya la busca propiamente
    #Busca por object list y se puede customizar
    #Puedo cambiarle el nombre
    context_object_name = 'appointments'
    
    #Vamos a generar una funcion dentro del appointment list para que el user tenga solo su propia data.
    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        # Vamos a sobreescribir con el context los appointments, que antes eran todas las citas, ahora se limitarán
        # En el template se hizo el request del user y ya con esto filtramos solo los appointments del user
        if(self.request.user.is_staff):
            context['appointments'] = context['appointments']
            return context
        else:
            context['appointments'] = context['appointments'].filter(user = self.request.user)
            return context
        


class AppointmentsDetail(LoginRequiredMixin, DetailView):
    model = Appointments
    #Tiene ese modelo asociado y busca por appointments_detail.html
    #Vamos a pasa el context object a appointment
    context_object_name = 'appointment'
    #Tambien puedo pasar al html que quiere ir, setear el template name
    template_name = 'appointments/appointment.html'

class AppointmentsCreate(LoginRequiredMixin, CreateView): #Estamos creando un dato, vista para creacion de dato
    #Va a buscar un _form.html
    model = Appointments #Utiliza este modelos
    #El create view por default da un model form para UTILIZAR, va a crear un FORM con el modelo
    fields = ['day', 'month', 'hour', 'description','user']

    #Si todo va bien redirija al usuario a donde ve todos sus appointments, send user back a ese url
    success_url = reverse_lazy('appointments')
    #El form que pasa DJANGO se llama form y lo recibe el html
    
    # Vamos a decirle al programa que solo el user que se encuentra puede crear para el mismo
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AppointmentsCreate, self).form_valid(form)
    # Si quiero realizar el cambio en _form, comento la funcion form_valid


class AppointmentsUpdate(LoginRequiredMixin, UpdateView):    
    model = Appointments
    fields = ['day', 'month', 'hour', 'description'] 
    #También cuando se hace, nos vamos a la lista de appointments
    success_url = reverse_lazy('appointments')
    #Por default busca el _form.html

#Con esto vamos a eliminar la cita
class AppointmentsDelete(LoginRequiredMixin, DeleteView):
    model = Appointments
    #Vamos a pasar el objeto como appointment
    context_object_name = 'appointment'
    #Si eliminamos vamos a volver a appointments (Lista general)
    success_url = reverse_lazy('appointments')
    #Por default se busca por un _confirm_delete.html