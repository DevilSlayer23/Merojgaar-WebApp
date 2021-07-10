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
 



class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    image = models.ImageField(upload_to='user/images/')

    skills = models.CharField(max_length=254)

    def __str__(self):
        return self.user.username

class Job(models.Model):
    title = models.CharField( max_length=150)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    description = models.TextField()
    salary_range = models.CharField( max_length=254)
    experience = models.CharField(max_length=100)
    seats_available = models.IntegerField()
    skills_required = models.CharField(max_length=254)

    def __str__(self):
        return self.title

