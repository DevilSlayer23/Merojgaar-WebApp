from django.shortcuts import render , redirect
from .forms import CompanyForm , JobForm ,JobApplyForm
from .models import Company , Job_category , Job

def register_company(request):
    if  request.method == "POST":
        form = CompanyForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("Company:company-login")
        
    return render(request, 'company/createcompany.html')

def login(request):
    if request.method == 'POST':
        user = Company.objects.all().get(username=request.POST.get('username'))
        if user.username == request.POST.get('username') and user.password == request.POST.get('password'):
            request.session['company'] = user.username
            request.session['id'] = user.id
            return redirect('Company:company-home')
    
    return render(request, 'candidate/login.html')

def add_jobs(request):
    cats = Job_category.objects.all()
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Company:company-home")
    context = {
        'id': request.session.get('id'),

        'company': request.session.get('company'),
        'cats':cats,
    }
    return render(request, 'company/add_jobs.html', context)


def company_home(request):
    category = Job_category.objects.all()
    company = request.session.get('id')
    jobs = Job.objects.all().filter(company=company)
    context = {
        'category': category,
        'jobs':jobs,
    }
    return render(request, 'company/home.html', context)

def company_logout(request):
   try:
      del request.session['username']
   except:
      pass
   return redirect('Main:index')

def job(request , id):
    job = Job.objects.all().get(id=id)

    context = {
        'job': job
    }

    return render(request ,'company/job.html', context)


def apply_job(request):
    if  request.method == "POST":
        apply_form = JobApplyForm(request.POST)

        if apply_form.is_valid():
            apply_form.save()

            return redirect('Candidate :home')
    context = {

    }
    return render(request, 'company/apply_job.html' , context)