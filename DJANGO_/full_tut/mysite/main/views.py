from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item
# всяка функция управлява една страница


# def index_page(response):
#     return HttpResponse("<h1>Hello Django</h1>")
    # http://localhost:8000/



def view_one(response):
    return HttpResponse("view one!")
    # http://localhost:8000/view_1/



def view_with_int(response, id):
    return HttpResponse("<p>%s</p>" % id)
    # http://localhost:8000/view_with_int/42


"ПОДАВАНЕ НА ТЕКСТ"
def todo_lst(response, name):
    lst = ToDoList.objects.get(name=name)
    item = lst.item_set.get(id=1)
    return HttpResponse("<p>%s</p> <br/> <p>%s</p>" %(lst.name, str(item.text)))
    # http://localhost:8000/todo_lst/My%20list



"ПОДАВАНЕ ПРОМЕНЛИВИ"
def var_page(response):
    dict = {
        "var_base": "var for BASE", 
        "var_home": "var for VAR_PAGE",
    }
    return render(response, "main/var_page.html", dict)



def list_page(response):
    lst = ToDoList.objects.all()
    return render(response, "main/list.html", {"lst_obj": lst})



"FORM"
from .forms import CreateNewList

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)                     # носи цялото инфо от попълнената форма

        if form.is_valid():                                     # ако е попълнена правилно
            t = ToDoList(name=form.cleaned_data["name"])       # създава нов обект
            t.save()                                            # и го пази
        return HttpResponse("%s" %t.name)                # показва готовия резултат

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
    # http://localhost:8000/create/



"CUSTOM FORMS"
# https://www.youtube.com/watch?v=sm1mokevMWk&ab_channel=TechWithTim
def custom(response, id):
    ls = ToDoList.objects.get(id=id)
    
    # {"save":["save"], "c1":["clicked"]}
    if response.method == "POST":           # взима dict с цялото инфо от формата
        print(response.POST)
        if response.POST.get("save"):        # взима името на бутона
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            # custom form, затова няма вградена проверка
            if len(txt) > 3:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")
    
    return render(response, "main.custom_form.html")
    # http://localhost:8000/custom/2





def index(response, id):
    ls = ToDoList.objects.get(id=id)
 
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                item.complete = True
            else:
                item.complete = False
    
            item.save()
    
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
    
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
    
    
        return render(response, "main/list.html", {"ls":ls})