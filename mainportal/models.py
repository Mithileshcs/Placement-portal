from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class CompanyRec(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    dept = models.CharField(max_length = 255)
    # Add other fields as needed

    def __str__(self):
        return f"{self.name} - {self.location} - {self.industry}"
    


class Profilenewmain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    backlogs = models.IntegerField(default=0)
    date_of_birth = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=100, blank=True)
    year_of_passing = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    

class JobApplication(models.Model):
    user_profile = models.ForeignKey('Profilenewmain', on_delete=models.CASCADE)
    company = models.ForeignKey('CompanyRec', on_delete=models.CASCADE)
    date_applied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.company.name}"