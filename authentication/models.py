from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone= models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)



class Department(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)


class Country(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=5, blank=True)
 
class Cities(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=5, blank=True)    
  