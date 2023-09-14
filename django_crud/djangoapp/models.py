from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_no = models.IntegerField()
