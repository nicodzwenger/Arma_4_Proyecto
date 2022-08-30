from django.db import models

class Usuarios(models.Model):
    email = models.EmailField()
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self) -> str:
        return 'EMAIL: %s - USUARIO: %s - CONTRASEÑA: %s' %(self.email, self.usuario, self.contraseña)