from django.urls import path
from .views import add_todo, complete_todo, completed_todos, delete_todo, edit_todo, todo_list, undo_todo


urlpatterns = [
    # 127.0.0.1:8000/todo/에서 할 일 목록을 볼 수 있도록 설정
    path("", todo_list, name="todo_list"),  # dev_2
    # 추가 기능을 위한 URL
    path('add/', add_todo, name='add_todo'), # dev_3
    # 완료 기능을 위한 URL (/todo/complete/1/)
    path('complete/<int:todo_id>/', complete_todo, name='complete_todo'),  # dev_4
    path('completed/', completed_todos, name='completed_todos'),    # dev_4
    path('edit/<int:todo_id>', edit_todo, name='edit_todo'),    # dev_5
    path('delete/<int:todo_id>', delete_todo, name='delete_todo'),    # dev_6
    path('undo/<int:todo_id>', undo_todo, name='undo_todo'),    # dev_7

]