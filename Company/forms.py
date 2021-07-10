
from django import forms
from .models import Company, Job



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


  