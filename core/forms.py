from django import forms
from django.forms import ModelForm
from .models import Anime
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AnimeForms(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Anime
        fields = ['nombre', 'capitulos', 'temporadas', 'genero', 'fecha_emision', 'sinopsis', 'imagen']

        widgets = {
            'fecha_emision':forms.SelectDateWidget(years=range(1990,2023))
        }
    
    def clean_fecha_emision(self):
        fecha = self.cleaned_data['fecha_emision']

        if fecha > datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser mayor al día de hoy")

        return fecha

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

