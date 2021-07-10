from django.urls import path
from . import views 
urlpatterns = [
    path('company-register' , views.register_company, name="company-register"),

]