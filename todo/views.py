from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from todo.models import Todo

# Create your views here.

# dev_2
def todo_list(request) : 
    # dev_10
    auto_delete_period = timezone.now() - timedelta(days=3)     # 완료한 todo 3일 뒤 삭제

    Todo.objects.filter(is_completed=True, created_at__lt=auto_delete_period).delete()

    # dev_2
    # todos = Todo.objects.all()   # 모든 todo 객체를 가져옴
    
    # dev_4
    # todos = Todo.objects.filter(is_completed = False)   # 미완료 todo 객체만 필터링

    # dev_8
    # todos = Todo.objects.filter(is_completed = False).order_by("-important", "created_at")  # 미완료 todo 객체를 중요순(내림차순) - 등록순(오름차순)으로 정렬
    
    # dev_9
    query = request.GET.get("q")  # 검색어 가져오기

    if query : 
        # 제목에 검색어가 포함된 할 일을 중요도순 - 등록순으로 정렬
        todos = Todo.objects.filter(is_completed = False, title__icontains=query).order_by("-important", "created_at")

    else : 
        # 검색어 없으면 전체 미완료 리스트
        todos = Todo.objects.filter(is_completed = False).order_by("-important", "created_at")

    return render(request, "todo/todo_list.html", {"todos" : todos})    # todo_list.html 파일을 렌더링하면서 할 일 목록을 전달

# dev_3 
def add_todo(request) : 
    # 사용자가 POST 요청을 보내면, 입력한 제목을 받아와서 새로운 할 일을 데이터베이스에 저장
    if request.method == "POST" : 
        title = request.POST.get("title")   # 폼에서 입력된 title 가져오기
        
        # dev_8
        important = request.POST.get("important") == "on"
        if title : 
            Todo.objects.create(title=title, important=important)    # title이 비어있지 않으면 새 할 일 저장
            print("할 일이 정상적으로 추가됨! 중요 : ", important)  # 터미널에서 확인
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
    
    

# dev_4    
def completed_todos(request):
    # dev_4
    # todos = Todo.objects.filter(is_completed=True)  # 완료순
    # todos = Todo.objects.filter(is_completed=True).order_by('-created_at')    # 생성순
    
    # dev_9
    query = request.GET.get("q")    # 검색어 가져오기

    if query: 
        todos = Todo.objects.filter(is_completed=True, title__icontains=query).order_by("-important", "created_at")
    else : 
        todos = Todo.objects.filter(is_completed=True)      # 검색어 없으면 모든 완료 리스트

    return render(request, "todo/completed_list.html", {"todos": todos})



# dev_5
def edit_todo(request, todo_id) : 
    todo = get_object_or_404(Todo, id = todo_id)
    
    if request.method == "POST" : 
        new_title = request.POST.get("title")

        # dev_8
        important = request.POST.get("important") == "on"

        if new_title :
            todo.title = new_title  # 제목 업데이트
            todo.important = important  # 중요 표시도 수정 가능     # dev_8
            todo.save() # DB에 반영
            return redirect("todo_list")    # 수정 후 다시 할 일 목록으로 이동
        
    return render(request, "todo/edit_todo.html", {"todo" : todo})


# dev_6
def delete_todo(request, todo_id) : 
    todo = get_object_or_404(Todo, id = todo_id)
    todo.delete()   # 바로 삭제해버림
    # 등록이나 수정은 save() 해야 하지만 삭제는 데이터베이스에서 해당 객체를 완전히 삭제해버리기 때문에 save()할 필요 없음
    # 필드 값을 변경하는 게 아닌 데이터 자체를 삭제
    return redirect("todo_list")


# dev_7
def undo_todo(request, todo_id) : 
    todo = get_object_or_404(Todo, id = todo_id)
    todo.is_completed = False   # 완료 상태 해제 (미완료로 변경)
    todo.save()
    return redirect("todo_list")    # 미완료 목록으로 이동