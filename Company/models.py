from django.db import models
from Candidate.models import Candidate
# Create your models here.

class Company(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    description = models.TextField()
    estd = models.DateField()
    email = models.CharField(max_length=60)
    contact = models.CharField(max_length=14)
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Job_category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Job(models.Model):
    types = [
        ('Full Time' , 'Full Time'), 
        ('Half Time' , 'Half Time'), 
        ('Temporary' , 'Temporary'), 
        ('Permanent' , 'Permanent'), 

    ]
    title = models.CharField( max_length=150)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    
    category = models.ForeignKey(Job_category, on_delete=models.CASCADE)
    description = models.TextField() 
    salary_range = models.CharField( max_length=254)
    experience = models.CharField(max_length=100)
    seats_available = models.IntegerField()
    skills_required = models.CharField(max_length=254)

    type = models.CharField(max_length=100 , choices=types, default="Full Time")


    def __str__(self):
        return self.title

class JobApply(models.Model):
    job = models.ForeignKey(Job , on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title