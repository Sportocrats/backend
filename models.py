from django.db import models

# Create your models here.

class Player_Male(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob=models.DateField()
    email=models.EmailField(max_length=254)
    password=models.TextField()
    sports=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name


