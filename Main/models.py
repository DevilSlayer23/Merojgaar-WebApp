from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    description = models.TextField()
    estd = models.DateField()
    email = models.CharField(max_length=60)
    contact = models.CharField(max_length=14)
    website = models.CharField(max_length=50)
    
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="company/logo/")

    def __str__(self):
        return self.name
 

class Skill(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add= True)
    def __str__(self):
        return self.name

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    image = models.ImageField(upload_to='user/images/')

    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.user.username
