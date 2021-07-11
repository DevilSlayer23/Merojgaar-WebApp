from django.shortcuts import render , redirect
from .forms import CompanyForm , JobForm
from .models import Company , Job_category , Job

def register_company(request):
    if  request.method == "POST":
        form = CompanyForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("Company:login")
        
    return render(request, 'company/createcompany.html')

def login(request):
    if request.method == 'POST':
        user = Company.objects.all().get(username=request.POST.get('username'))
        if user.username == request.POST.get('username') and user.password == request.POST.get('password'):
            request.session['company'] = user.username
            return redirect('Company:company-home')
    
    return render(request, 'Company/login.html')

def add_jobs(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Company:company-home")
    
    return render(request, 'company/add_jobs.html')


def company_home(request):
    category = Job_category.objects.all()
    context = {
        'user' : request.session.get('user'),
        'category': category,
    }
    return render(request, 'company/home.html', context)

def company_logout(request):
   try:
      del request.session['username']
   except:
      pass
   return redirect('Main:index')