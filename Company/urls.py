from django.urls import path
from . import views 
urlpatterns = [
    path('company-register/' , views.register_company, name="company-register"),
    path('add-jobs/', views.add_jobs, name="add-jobs"),
    path('company-login/', views.login, name="company-login"),
    path('company-home/', views.company_home, name="company-home"),
    path('company-logout/', views.company_logout, name="company-logout"),

]