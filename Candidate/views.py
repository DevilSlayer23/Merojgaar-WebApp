from django.shortcuts import render , redirect
from .forms import UserForm 
from django.contrib.auth import login
from django.contrib import messages


def register_candidate(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request , user)
            
            request.session['user'] = user
            messages.success(request , "Registration Success")
            return  redirect("Main:index")
        messages.error(request , "Regsitraion unsucsessfull")
    form = UserForm()
    context = {
        'form' : form
    }
    return render(request , 'candidate/register.html' , context)
