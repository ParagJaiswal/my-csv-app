from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.first_name