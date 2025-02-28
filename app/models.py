from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True,null=True)
    text = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} {self.title} - {self.text[:10]}'