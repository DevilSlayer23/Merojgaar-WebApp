from .models import Company , Job
from django import forms


class CompanyForm(forms.ModelForm):
  class Meta:
    model = Company
    exclude = ['user']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

  