from django.urls import path
from .views import add_todo, todo_list


urlpatterns = [
    # 127.0.0.1:8000/todo/에서 할 일 목록을 볼 수 있도록 설정
    path("", todo_list, name="todo_list"),  # dev_2
    # 추가 기능을 위한 URL
    path('add/', add_todo, name='add_todo'), # dev_3
    
]