from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField(auto_now=False, auto_now_add=True)
  isDone = models.BooleanField(default=False)
  user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)