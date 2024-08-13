from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.

# регистриране на модела, за да е достъпен от админ панела
admin.site.register(ToDoList)
admin.site.register(Item)