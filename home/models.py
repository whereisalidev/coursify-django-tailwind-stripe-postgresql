from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads')
    is_paid = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
