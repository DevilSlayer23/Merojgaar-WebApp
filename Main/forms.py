from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Company
from django import forms

class UserForm(UserCreationForm):
    email = forms.CharField(max_length=50 ,required=True)

    user_type_choices = [
        ('Organaization' , "Organaization"),
        ('JS', 'Job Seeker')

    ]

    user_type = forms.CharField(max_length=15 , required=True)
    class Meta:
        model = User
        fields = ('first_name' , 'last_name','username' , 'email' , 'password' , 'password2')

    def save(self , commit=True):
        user = super(UserForm , self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']

        if commit:
            user.save()
        return user

class CompanyForm(forms.ModelForm):
  class Meta:
    model = Company
    exclude = ['user']

  