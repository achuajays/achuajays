from django.db import models


class head(models.Model):
    e = models.EmailField()
    p = models.CharField(max_length=100)


class book(models.Model):
    bi = models.IntegerField(primary_key=True)
    bn = models.CharField(max_length=100)
    an = models.CharField(max_length=100)
    sn = models.IntegerField()


      


class bookr(models.Model):
    bi = models.IntegerField(primary_key=True)
    bn = models.CharField(max_length=100)
    an = models.CharField(max_length=100)
    si = models.IntegerField()
    e = models.EmailField(default= 'fibj@gmail.com')
    se = models.DateField()
    st = models.CharField(max_length=1 , default='f')
    sname = models.IntegerField(default = 1)








class bookre(models.Model):
    bi = models.IntegerField(primary_key=True)
    bn = models.CharField(max_length=100)
    an = models.CharField(max_length=100)
    sn = models.IntegerField()
