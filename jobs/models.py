from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    cost = models.IntegerField()
    year = models.DateField(null=True, blank=True)

