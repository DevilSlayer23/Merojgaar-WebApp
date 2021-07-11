from django.shortcuts import render , redirect
from .forms import   CandidateForm
from .models import Candidate , CandidateSkill 
from Company.models import Job_category, Job
from .forms import CandidateSkillForm


def register_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
       
        if form.is_valid():
            form.save()
            return redirect('Candidate:login') 

    return render(request , 'candidate/register.html')

def login(request):
    if request.method == 'POST':
        user = Candidate.objects.all().get(username=request.POST.get('username'))
        if user.username == request.POST.get('username') and user.password == request.POST.get('password'):
            request.session['username'] = user.username
            print(request.session['username'])
            return redirect('Candidate:home')
    
    return render(request, 'candidate/login.html')


def home(request):
    
    if request.method == "POST":
        skill = CandidateSkillForm(request.POST)
        if skill.is_valid():
            skill.save()
            return redirect('Candidate:home')

    category = Job_category.objects.all()
    
    jobs = Job.objects.all()
    candidate = Candidate.objects.all().get(username=request.session.get('username'))
    skills = CandidateSkill.objects.all().filter(candidate=candidate.id)
    
    context = { 
        'candidate' : candidate,
        'category': category,
        'jobs': jobs,
        'skills':skills,
    }
    return render(request , 'candidate/home.html', context)

def candidate_logout(request):
   try:
      del request.session['username']
   except:
      pass
   return redirect('Main:index')