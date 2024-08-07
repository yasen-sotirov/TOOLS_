from django.shortcuts import render, HttpResponse
from .models import TodoItem    # импорт от базата данни

# Create your views here.

def home(request):                          # request - дава достъп до query param и body 
    return render(request, "home.html")
    # трябва да се направи път за тази функция в urls.py
    # HttpResponse - връща прости данни, без рендване


def todos(request):
    items = TodoItem.objects.all()      # взема всички обекти от БД в това поле
    return render(request, "todos.html", {"todos": items }) 
    # списъка с todos, който подавам на html да луупва == items
    # трябва да се направи път за тази функция в urls.py