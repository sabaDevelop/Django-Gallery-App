from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    caption=models.TextField(blank = True, max_length=200)
    image=models.ImageField(upload_to="img/%y")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
