from django.urls import path
from todo_app import views


urlpatterns = [
    path('todo-lists', views.todo_lists_handler)
    # path('todo-lists/<int:pk>', views.),
    # path('todo-lists/<int:pk>/todos'),
    # path('todos'),
    # path('todos/<int:pk>')

]