from django.db import models
from django.contrib.auth.admin import User

# Create your models he
class caretaker(models.Model):
    LOGIN=models.OneToOneField(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    photo=models.FileField()
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)

class blind(models.Model):
    CARETAKER=models.ForeignKey(caretaker,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    imei=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()

class Complaints(models.Model):
    CARETAKER=models.ForeignKey(caretaker,on_delete=models.CASCADE)
    comp=models.CharField(max_length=500)
    date=models.DateField()
    reply=models.CharField(max_length=500)

class location(models.Model):
    BLIND=models.ForeignKey(blind,on_delete=models.CASCADE)
    latitude=models.BigIntegerField()
    longitude=models.BigIntegerField()

class help(models.Model):
    BLIND = models.ForeignKey(blind, on_delete=models.CASCADE)
    latitude = models.BigIntegerField()
    longitude = models.BigIntegerField()
    date=models.DateField()

class familiar_person(models.Model):
    BLIND = models.ForeignKey(blind, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    relation=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()

class object_table(models.Model):
    Name=models.CharField(max_length=100)
    image=models.FileField()
    details=models.CharField(max_length=500)


