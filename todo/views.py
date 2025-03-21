from django.shortcuts import render

from todo.models import Todo

# Create your views here.

# dev_2
def todo_list(request) : 
    todos = Todo.objects.all()   # 모든 todo 객체를 가져옴
    return render(request, "todo/todo_list.html", {"todos" : todos})    # todo_list.html 파일을 렌더링하면서 할 일 목록을 전달

