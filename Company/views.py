from django.shortcuts import render , redirect
from .forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register_company(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            messages.success(request , "Registration Success")
            return  redirect("Main:index")
        messages.error(request , "Regsitraion unsucsessfull")
    form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request , 'company/company_register.html' , context)

