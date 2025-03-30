from django.db import models

# Create your models here.
class Entry(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Data1 = models.CharField(max_length=50, default="")
    Data2 = models.CharField(max_length=50, default="")
    
    def __str__(self):
        return self.Data1
