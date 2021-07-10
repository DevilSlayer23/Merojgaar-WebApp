from django.db import models

# Create your models here.
class CandidateDetails(models.Model):
    
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    image = models.ImageField(upload_to='user/images/')
    skills = models.CharField(max_length=254)

    def __str__(self):
        return self.user.username
