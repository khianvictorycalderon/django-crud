from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {
        "todos": items
    })

def create_todos(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("Todos")
    
    return render(request, "create_todo.html", { "form": form })

def edit_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)

    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        form.save()
        return redirect("Todos")
    
    return render(request, "edit_todo.html", { "form": form, "todo": todo })