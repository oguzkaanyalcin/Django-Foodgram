from django.db import models
from ckeditor.fields import RichTextField

class Categories(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True, max_length=50)
    image_url = models.CharField(default="", max_length=50)

    def __str__(self):
        return f"{self.name} ({self.slug})"
    
class Food(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default="")
    description = RichTextField()
    image_url = models.CharField(max_length=50)
    date = models.DateField()
    isUpdate = models.BooleanField()
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return f"{self.title} ({self.date})"