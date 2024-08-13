from django.urls import path
from . import views             # от същата дир вкарва файла view


urlpatterns = [
    # path("", views.index_page),      
    # ако влезем в сайта на индекс / "", това ще ни изпрати на views.index
    # името се използва в .html за рефериране:  <a href="{% url 'index' %}"

    path("", views.index_page),  


    path("view_1/", views.view_one),

    path("view_with_int/<int:id>", views.view_with_int),
    # ще подаде id (int) на пътеката към view
    
    path("todo_lst/<str:name>", views.todo_lst),


    path("var/", views.var_page, name="var_page"),

    path("list/", views.list_page, name="list"),

    path("create/", views.create, name="create"),

    path("custom/", views.custom, name="custom"),

]
