from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')])
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=[('efectivo', 'Efectivo'), ('bancaria', 'Bancaria')])
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')])
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto}"
