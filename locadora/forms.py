# forms.py
from django.forms import ModelForm, EmailField, CharField
from .models import Car, User, Reservation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'year', 'is_available', 'price', 'avatar']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname','phone_number','cpf','connect']
        


    

class ReservationForm(ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        # Limita as opções de usuário (cliente) e carro nas opções do formulário
        self.fields['user'].queryset = User.objects.all()
        self.fields['car'].queryset = Car.objects.filter(is_available='Disponível')
    


    class Meta:
        model = Reservation
        fields = ['user', 'car', 'pickup_date', 'return_date']



class RegistrationForm(UserCreationForm):
    
    first_name= CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=200, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username','first_name', 'last_name','email', 'password1', 'password2' ]


    
