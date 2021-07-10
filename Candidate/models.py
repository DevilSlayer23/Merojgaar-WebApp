from django.db import models

# Create your models here.
class Candidate(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return self.username
    
class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.skill

