from django.urls import path
from . import views 
urlpatterns = [
    path('register/' , views.register_candidate, name="candidate-register"),
    path('login/' , views.login, name="login"),
    path('home/' , views.home , name="home"),
    path('candidate-logout' , views.candidate_logout , name="candidate-logout"),
]