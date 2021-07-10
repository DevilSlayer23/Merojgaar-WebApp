from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CompanyForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' ,  'password' , 'password2')

    def save(self , commit=True):
        company = super(CompanyForm , self).save(commit=False)
        if commit:
            company.save()
        return company

  