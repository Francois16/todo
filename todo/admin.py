from django.contrib import admin

# Models
from .models import Todo, Category


admin.site.register(Todo)
admin.site.register(Category)
