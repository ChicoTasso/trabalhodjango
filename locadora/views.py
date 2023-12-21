from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CarForm, RegistrationForm, ReservationForm
from .models import Car, Reservation
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin




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

class CarCreateView(LoginRequiredMixin,CreateView):
    model = Car
    form_class = CarForm
    template_name = 'carros/car_form.html'
    success_url = reverse_lazy('car_list')
    

class CarUpdateView(LoginRequiredMixin,UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'carros/car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(LoginRequiredMixin,DeleteView):
    model = Car
    template_name = 'carros/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')

class UserListView(ListView):
    model = get_user_model()
    template_name = 'usuários/user_list.html'
    context_object_name = 'user'

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'usuários/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'usuários/user_form.html'
    success_url = '/users/'  

class UserUpdateView(UpdateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'usuários/user_form.html'
    success_url = reverse_lazy('user_list')  

class UserDeleteView(DeleteView):
    model = get_user_model()
    template_name = 'usuários/user_confirm_delete.html'
    success_url = '/users/'

class ReservationListView(LoginRequiredMixin,ListView):
    model = Reservation
    template_name = 'reservas/reservation_list.html'
    context_object_name = 'reservations'

class ReservationDetailView(LoginRequiredMixin,DetailView):
    model = Reservation
    template_name = 'reservas/reservation_detail.html'
    context_object_name = 'reservation'

class ReservationCreateView(LoginRequiredMixin,CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservas/reservation_form.html'
    success_url = '/reservations/'
        
    def reserve_car(request, car_id):
        car = get_object_or_404(Car, pk=car_id)

        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.car = car
                reservation.user = request.user  
                reservation.save()

                car.status = 'Alugado'
                car.save()

                return redirect('reservation_list')  
        else:
            form = ReservationForm()

        return render(request, 'reserve_car.html', {'form': form, 'car': car})

class ReservationUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservas/reservation_form.html'
    success_url = '/reservations/'  

class ReservationDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
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
    