from django.contrib import admin
from .models import Categoria, Cuenta, Movimiento

admin.site.register(Categoria)
admin.site.register(Cuenta)
admin.site.register(Movimiento)