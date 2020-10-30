from django.db import models


# Create your models here.
class entrie(models.Model):
    name=models.CharField(max_length=220)
    address=models.TextField(max_length=220)
    phone=models.CharField(max_length=20)
    pincoe=models.CharField(max_length=10)

    def __str__(self):
        return self.name
