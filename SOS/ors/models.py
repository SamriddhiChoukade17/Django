from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    loginId = models.CharField(max_length = 50)
    password = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        db_table  = 'sos_user'



class Marksheet(models.Model):
    fullName = models.CharField(max_length = 50)
    rollNo = models.IntegerField(max_length = 50)
    physics = models.IntegerField(max_length = 50)
    chemistry = models.IntegerField(max_length=50)
    maths = models.IntegerField(max_length=50)
    #address = models.CharField(max_length=50)

    class Meta:
        db_table  = 'sos_marksheet'
