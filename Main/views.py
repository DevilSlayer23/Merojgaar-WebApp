from django.shortcuts import render , redirect
from .forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import CompanyForm

# Create your views here.


def register_user(request):
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
    return render(request , 'Main/register.html' , context)

def index(request):
    return render(request , 'Main/index.html')

def register_comp(request):
    if request.method == "POST":
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return redirect("Main:index")
        messages.error(request, "Company Registration Failed")
    
    company_form = CompanyForm()
    context = {
        'company_form' : company_form,
    }
    return render(request, 'Main/index.html', context)
