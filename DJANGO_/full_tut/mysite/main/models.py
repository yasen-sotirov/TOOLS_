from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField( max_length=100)

    def __str__(self) -> str:
        return self.name
    


class Item(models.Model):
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)   
    # ако бъде изтрит ключа, ще изтрие всички свързани с него
    text = models.CharField(max_length=300)
    completed = models.BooleanField()

    def __str__(self) -> str:
        return self.text