from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo
    template_name = 'home.html'


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = '__all__'   
    success_url = reverse_lazy('home') 


class TodoUpdateView(UpdateView): 
    model = Todo
    template_name = 'todo_edit.html'
    fields = ['title', 'description']    
    success_url = reverse_lazy('home')


class TodoDeleteView(DeleteView): 
    model = Todo 
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')    