from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]
        labels = {
            'username':'Nombre de usuario:',
            'password':'Contraseña:',
            'email':'Correo:',
        }