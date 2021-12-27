from django.urls import path

# Views
from .views import todo_deleteview, todo_listview, todo_createview, todo_updateview

urlpatterns = [
    path("", todo_listview, name="todo_listview"),
    path("add/", todo_createview, name="new_todo"),
    path("<uuid:pk>/delete/", todo_deleteview, name="todo_delete"),
    path("<uuid:pk>/update/", todo_updateview, name="todo_update"),
]
