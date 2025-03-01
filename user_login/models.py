from django.db import models

# Create your models here.
class Sign_up(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    Phonenumber = models.IntegerField(max_length=10)
    password = models.CharField(max_length=100)
    confirm_password= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} {self.email} {self.password}"


