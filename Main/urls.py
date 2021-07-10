from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('register/', views.register_user ,name ="register"),
    path('register-comp/', views.register_comp ,name ="register-comp")
]