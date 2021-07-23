from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    

    def __str__(self):
        return self.contact


class Address(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    

    def __str__(self):
        return self.address
