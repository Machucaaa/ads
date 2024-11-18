from django.contrib import admin

from .models import Categoria, Producto, Cart, Orden
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cart)
admin.site.register(Orden)