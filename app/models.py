from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    cnicNo = models.CharField(max_length=13, unique=True)






