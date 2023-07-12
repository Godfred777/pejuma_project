from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.user.username
    

class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    geo_coverage = models.CharField(max_length=100, blank=True)
    expertise = models.CharField(max_length=100)
    rating = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return self.user.username
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)

class Reviews(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)