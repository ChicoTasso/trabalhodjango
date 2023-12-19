# forms.py
from django.forms import ModelForm, EmailField, CharField, ImageField
from .models import Car, Reservation
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CarForm(ModelForm):


    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'year', 'is_available', 'price', 'avatar']
    
    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': 'form-control-file'})


    

class ReservationForm(ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = get_user_model().objects.all()
        self.fields['car'].queryset = Car.objects.filter(is_available='Disponível')
    


    class Meta:
        model = Reservation
        fields = ['user', 'car', 'pickup_date', 'return_date']



class RegistrationForm(UserCreationForm):
    
    first_name= CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=200, label="Email")
    cpf = CharField(max_length=11,label='CPF')
    phone_number = CharField(max_length=20,label='N° de Telefone')
    
    class Meta:
        model = get_user_model()
        fields=['username','first_name', 'last_name','cpf','phone_number','email', 'password1', 'password2' ]
        


    
