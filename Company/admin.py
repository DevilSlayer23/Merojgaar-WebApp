from django.contrib import admin
# Register your models here.
from .models import Company, Job , Job_category , JobApply

admin.site.register(Company)

admin.site.register(Job)
admin.site.register(Job_category)
admin.site.register(JobApply)