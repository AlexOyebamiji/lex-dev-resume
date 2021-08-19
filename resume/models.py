from django.db import models

# Create your models here.
class messageInsert(models.Model):
    nameInsert = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    yourMessage = models.CharField(max_length=100)

    def __str__(self):
        return self.nameInsert