from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=40)
    comp_name = models.CharField(max_length=40)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    url = models.CharField(max_length=100,null=True,blank=True)
    data = models.DateField()
    text = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')

class Murojat(models.Model):
    ism = models.CharField(max_length=30)
    pochta = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    data = models.DateTimeField(auto_now=True)


class team(models.Model):
    nomi = models.CharField(max_length=30)
    lavozim = models.CharField(max_length=30)
    text = models.TextField()
