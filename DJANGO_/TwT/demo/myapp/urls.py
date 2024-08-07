from django.urls import path
from . import views

# ANCHOR оказва пътя на url в аппа

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")       # http://localhost:8000/todos/
]

    # "todos/"          - префикс
    # views.todos,      - къде се намира
    # name="Todos")     - как се казва
