from django.db import models
import datetime

class players(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
    signed=models.DateField(null=False,default=datetime.date.today)



