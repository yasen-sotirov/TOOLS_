from django.contrib import admin
from .models import TodoItem        # класа модел който създадох

# Register your models here.
# Тук се регистрират ORM моделите 

admin.site.register(TodoItem)

# след регистрацията се прави миграция - превръща новия код в таблици в бд
# python manage.py makemigrations       - създава миграцията
# python manage.py migrate              - прилага миграцията и ъпдейтва БД

