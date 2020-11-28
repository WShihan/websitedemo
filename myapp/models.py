from django.db import models

# Create your models here.
class ViewNum(models.Model):
    name = models.CharField(max_length=15)
    num = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
    code = models.CharField(max_length=15 ,unique=True)
    pack_size = models.CharField(max_length=5)
    address = models.CharField(max_length=15)
    date = models.CharField(max_length=20)
    note = models.CharField(max_length=50)

class Test(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
    code = models.CharField(max_length=15, unique=True)
    pack_size = models.CharField(max_length=5)
    address = models.CharField(max_length=15)
    date = models.CharField(max_length=20)
    note = models.CharField(max_length=50)

class TakeOut(models.Model):
    name = models.CharField(max_length=20)
    where = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=10)
    note = models.CharField(max_length=50)
    date = models.CharField(max_length=20)

class Soft(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    soft = models.CharField(max_length=20)
    note = models.CharField(max_length=50)
    date = models.CharField(max_length=20)

class Saying(models.Model):
    saying = models.CharField(max_length=300)

class One(models.Model):
    saying = models.CharField(max_length=400)
    url = models.CharField(max_length=50)
    day = models.CharField(max_length=6)
    date =  models.CharField(max_length=8)

class FeedBack(models.Model):
    content = models.CharField(max_length=200)
    email = models.CharField(max_length=40)
    date = models.CharField(max_length=20)
