from django import forms
from .models import  Candidate , CandidateSkill

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

class CandidateSkillForm(forms.ModelForm):
    class Meta:
        model = CandidateSkill
        fields = '__all__'

