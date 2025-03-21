from django.shortcuts import get_object_or_404, redirect, render

from todo.models import Todo

# Create your views here.

# dev_2
def todo_list(request) : 
    todos = Todo.objects.all()   # 모든 todo 객체를 가져옴
    return render(request, "todo/todo_list.html", {"todos" : todos})    # todo_list.html 파일을 렌더링하면서 할 일 목록을 전달

# dev_3 
def add_todo(request) : 
    # 사용자가 POST 요청을 보내면, 입력한 제목을 받아와서 새로운 할 일을 데이터베이스에 저장
    if request.method == "POST" : 
        title = request.POST.get("title")   # 폼에서 입력된 title 가져오기
        
        if title : 
            Todo.objects.create(title=title)    # title이 비어있지 않으면 새 할 일 저장
            print("할 일이 정상적으로 추가됨!")  # 터미널에서 확인
        else:
            print("제목이 비어 있어서 추가되지 않음!")  # 터미널에서 확인
        
        # urls.py에서 name="todo_list"로 등록한 URL로 redirect
        return redirect("todo_list")
    
    return render(request, "todo/add_todo.html")  # GET 요청 시 폼을 보여줌

# dev_4
def complete_todo(request, todo_id) : 
    # 지정한 객체를 가져오되, 없으면 404 에러
    # http://127.0.0.1:8000/todo/complete/999/ => id=999인 todo가 없으면 에러
    # get_object_or_404를 통해 자동으로 404 페이지로 이동
    
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = True
    todo.save()
    return redirect("todo_list")