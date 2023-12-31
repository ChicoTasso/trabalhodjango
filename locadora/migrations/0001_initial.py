# Generated by Django 4.2.8 on 2023-12-15 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, choices=[('Preto', 'Preto'), ('Prata', 'Prata'), ('Vermelho', 'Vermelho'), ('Branco', 'Branco')], max_length=30)),
                ('year', models.PositiveSmallIntegerField()),
                ('price', models.PositiveBigIntegerField()),
                ('is_available', models.CharField(choices=[('Disponível', 'Disponível'), ('Alugado', 'Alugado')], default='Disponível', max_length=30)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11)),
                ('connect', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.user')),
            ],
        ),
    ]
