from django.contrib import admin
from netflix.models import Movie
from netflix.models import Category
from netflix.models import Tag

admin.site.register(Category)
admin.site.register(Tag)
