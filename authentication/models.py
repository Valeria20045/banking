from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} {self.abrev}{'Activate' if self.status else 'inactive'}"

class Department(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=5)
    id_country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    #def __str__(self):
    #    return f"{self.name} {self.abrev}"
     

class Cities(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=5, blank=True)  
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name_cities = models.CharField(max_length=5)
    abrev = models.TextField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #def __str__(self):
     #   return f"{self.name} {self.abrev}"
   
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
    id_city = models.ForeignKey(Cities, on_delete=models.CASCADE)



 
  
  