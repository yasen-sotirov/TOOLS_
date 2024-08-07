from django.db import models

# Create your models here.
# СЪЗДАВА ORM МОДЕЛИ КОИТО ПРАВЯТ ТАБЛИЦИ В БАЗАТА ДАННИ

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    competed = models.BooleanField(default=False)

    # моделът трябва да бъде регистриран в app > admin
