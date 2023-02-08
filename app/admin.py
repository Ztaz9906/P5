from django.contrib import admin

# Register your models here.
from .models import Planilla,MedioBasico,User

# Register the admin class with the associated model
admin.site.register(User)
admin.site.register(Planilla)
admin.site.register(MedioBasico)