from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Correo', help_text='Es necesario que sea menor a 150 caracteres')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { key: '' for key in fields }


class EditarUsuarioForm(forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    avatar = forms.ImageField(required=False)