from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserForm,CarForm, RegistrationForm, ReservationForm
from .models import Car,User, Reservation
from django.contrib.auth import get_user_model




# Create your views here.

def home (request):
    return render(request, 'home.html')
def base (request):
    return render(request, 'base.html')

class CarListView(ListView):
    model = Car
    template_name = 'carros/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'carros/car_detail.html'
    context_object_name = 'car'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'carros/car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'carros/car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'carros/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')

class UserListView(ListView):
    model = User
    template_name = 'usuários/user_list.html'
    context_object_name = 'user'

class UserDetailView(DetailView):
    model = User
    template_name = 'usuários/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'usuários/user_form.html'
    success_url = '/users/'  

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'usuários/user_form.html'
    success_url = reverse_lazy('user_list')  

class UserDeleteView(DeleteView):
    model = User
    template_name = 'usuários/user_confirm_delete.html'
    success_url = '/users/'

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservas/reservation_list.html'
    context_object_name = 'reservations'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservas/reservation_detail.html'
    context_object_name = 'reservation'

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservas/reservation_form.html'
    success_url = '/reservations/'  

class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservas/reservation_form.html'
    success_url = '/reservations/'  

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservas/reservation_confirm_delete.html'
    success_url = '/reservations/'  
def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = RegistrationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')