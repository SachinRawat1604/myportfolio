# portfolio/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/') 

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='certifications/',null=True, blank=True)  

    def __str__(self):
        return f"{self.title} – {self.issuer}"
