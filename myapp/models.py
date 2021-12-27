from django.db import models

# Create your models here.

class Qabul(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.phone
    