from django.contrib import admin
from .models import Article
from .models import Author
# Register your models here.
admin.site.register([Article, Author])
