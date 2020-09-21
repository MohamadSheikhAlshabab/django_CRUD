from django.urls import reverse
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    
    def __str__(self): 
        return self.title 
    
    def get_absolute_url(self):
        return reverse('home')