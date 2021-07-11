from django.contrib import admin

# Register your models here.
from .models import Candidate , CandidateSkill

admin.site.register(Candidate)
admin.site.register(CandidateSkill)