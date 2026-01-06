from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("todos/create/", views.create_todos, name="create_todo"),
    path("todos/edit/<int:pk>/", views.edit_todo, name="edit_todo")
]