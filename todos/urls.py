
from django.urls import include, path

from todos.views import todo_list

urlpatterns = [
    path('', todo_list, name='todo_list'),
]
