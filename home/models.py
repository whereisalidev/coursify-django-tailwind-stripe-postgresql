from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    free = models.BooleanField(default=False)
    enrolled = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True) 

    def __str__(self):
        return self.name
    

