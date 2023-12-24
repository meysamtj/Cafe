from django.contrib import admin
from .models import Category, MenuItem, Image
# Register your models here.
admin.site.register([Category, MenuItem, Image])