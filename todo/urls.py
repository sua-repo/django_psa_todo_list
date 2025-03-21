from django.urls import path
from .views import todo_list


urlpatterns = [
    # 127.0.0.1:8000/todo/에서 할 일 목록을 볼 수 있도록 설정
    path("", todo_list, name="todo_list"),  # dev_2
    
]