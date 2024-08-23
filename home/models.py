from django.db import models
from django.utils.text import slugify



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True) 
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

