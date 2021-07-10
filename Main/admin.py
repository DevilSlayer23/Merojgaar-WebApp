from django.contrib import admin

# Register your models here.
from .models import Company , UserDetails , Job

admin.site.register(Company)
admin.site.register(UserDetails)
admin.site.register(Job)