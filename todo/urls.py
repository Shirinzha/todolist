from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('new/', TodoCreateView.as_view(), name='post_new'),
    path('edit/<int:pk>/', TodoUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='post_delete'),
]
