from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import Car, Maintenance

# Register your models here
admin.site.register(Car)
admin.site.register(Maintenance)