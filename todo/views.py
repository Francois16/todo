from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Prefetch

# Models
from .models import Todo, get_users_todos, Category

# Forms
from .forms import NewTodoForm, UpdateTodoForm


def todo_listview(request):

    template_name = "todos/listview.html"
    context = {
        "categories": Category.objects.prefetch_related(
            Prefetch("todo_set", queryset=get_users_todos(user=request.user), to_attr="user_todos")
        ),
    }
    return render(request, template_name, context)


def todo_createview(request):

    template_name = "todos/createview.html"

    if request.method == "POST":
        form = NewTodoForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("todo_listview")

    else:
        form = NewTodoForm()

    context = {
        "form": form,
    }

    return render(request, template_name, context)


def todo_deleteview(request, pk):

    if request.method == "POST":
        Todo.objects.filter(id=pk).delete()

    return redirect("todo_listview")


def todo_updateview(request, pk):

    template_name = "todos/updateview.html"

    if request.method == "POST":
        todo = get_object_or_404(Todo, id=pk)
        form = UpdateTodoForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            return redirect("todo_listview")

    else:
        form = UpdateTodoForm(instance=get_object_or_404(Todo, id=pk))

    context = {
        "form": form,
    }

    return render(request, template_name, context)
