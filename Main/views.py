from django.shortcuts import render , redirect
from Company.models import Job_category , Job 
from Candidate.forms import CandidateSkillForm
from Candidate.models import Candidate , CandidateSkill
# Create your views here.


def index(request):
    if request.session.has_key('username'):
        return redirect('Candidate:home')
        
    else:
        category = Job_category.objects.all()
        jobs = Job.objects.all()
        context = { 
            'category': category,
            'jobs': jobs,
            
        }
        return render(request , 'main/index.html', context)


