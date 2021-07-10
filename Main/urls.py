from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('register-comp/', views.register_comp ,name ="register-comp"),
    path('job-form/', views.job_form, name ="job-form"),
]