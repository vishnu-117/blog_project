from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('auth.USER',on_delete=models.CASCADE)
    body = models.TextField(default="enter some text")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    