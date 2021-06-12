from django.urls import path
from .views import AppointmentsList, AppointmentsDetail, AppointmentsCreate, AppointmentsUpdate, AppointmentsDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = "login"), 
    #Esto va a tomar el view de logout directamente, y lo va a llevar al login page, debo pasarlo en el html el brinca a logout y seguido a login
    path('logout/', LogoutView.as_view(next_page = 'login'), name = "logout"),
    path('register/', RegisterPage.as_view(), name = "register"),
    path('', AppointmentsList.as_view(), name = "appointments"), 
    path('appointment/<int:pk>', AppointmentsDetail.as_view(), name = "appointment"), #Url para un appointment especifico
    path('appointment-create', AppointmentsCreate.as_view(), name = "appointment-create"), #URL para crear nuevo appointment
    path('appointment-update/<int:pk>', AppointmentsUpdate.as_view(), name = "appointment-update"), #Vamos a hacer el update de un task especifico
    path('appointment-delete/<int:pk>', AppointmentsDelete.as_view(), name = "appointment-delete"),
]