from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """Category model class."""
    name = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    watch_count = models.IntegerField(default=0)
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name