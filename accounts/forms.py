from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    pwd_1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    pwd_2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "pwd_1", "pwd_2"]
