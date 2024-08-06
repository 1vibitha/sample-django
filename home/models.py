from django.db import models

# Create your models here.
class Department(models.model):
    dept_name=models.CharField(max_length=100)
    dept_description=models.TextField()
    