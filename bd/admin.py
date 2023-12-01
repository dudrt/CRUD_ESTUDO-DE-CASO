from django.contrib import admin
from .models import Garçom , Gerente
# from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Gerente)
admin.site.register(Garçom)
# admin.site.register(CustomUser)