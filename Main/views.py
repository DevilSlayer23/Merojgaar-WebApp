from django.shortcuts import render , redirect
from .forms import  JobForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import CompanyForm

# Create your views here.
from .models import Company 


def index(request):
    return render(request , 'main/index.html')

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
    return render(request, 'main/index.html', context)


def job_form(request):
    company = Company.objects.all()
    if request.method == 'POST':
        jobForm = JobForm(request.POST)
        if jobForm.is_valid():
            jobForm.save()
            print("done")
            return redirect('Main:job-form')
    context = {
        'company': company,
        
    }
    return render(request, 'main/job.html', context)
