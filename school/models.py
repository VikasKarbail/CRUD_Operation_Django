

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True, auto_created=True)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

