from django.db import models

class student(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.CharField(max_length=10,default="patna")
    marks = models.IntegerField(default=10)
    # date = models.DateField(default='1-1-2019')


    def __str__(self):
        return self.name

# Create your models here.
