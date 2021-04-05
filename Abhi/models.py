from django.db import models

# Create your models here.

class Admin(models.Model):
    voucher = models.CharField(max_length=10,primary_key=True)
    facevalue = models.IntegerField()
    startdate = models.DateTimeField() 
    enddate = models.DateTimeField() 
class Mobile(models.Model):
    admi = models.ForeignKey(Admin,on_delete = models.CASCADE,related_name='mob_set')
    mob = models.IntegerField()
    