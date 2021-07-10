from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' ,  'password' , 'password2')

    def save(self , commit=True):
        user = super(UserForm , self).save(commit=False)

        if commit:
            user.save()
            
        return user
