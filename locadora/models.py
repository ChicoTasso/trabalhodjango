from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from carros import settings

# Create your models here.


    
class Car(models.Model):
    STATUS = (
        ('Disponível', 'Disponível'),
        ('Alugado','Alugado'),
    )
    COR = (
        ('Preto','Preto'),
        ('Prata','Prata'),
        ('Vermelho','Vermelho'),
        ('Branco','Branco')
    )
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(
        max_length=30,
        choices=COR,
        blank=True,
    )
    year = models.PositiveSmallIntegerField()
    price = models.PositiveBigIntegerField() 
    is_available = models.CharField(
        max_length=30,
        choices=STATUS,
        default='Disponível',
    )
    avatar = models.ImageField('Picture', upload_to='avatares',blank=True, null=True)




    def __str__(self):
        return f"{self.brand} - {self.model} - {self.color}"
    


    
# models.py


class Reservation(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    
    def __str__(self):
        return f" {self.user} - {self.car.brand} - {self.car.model} - {self.car.color}"