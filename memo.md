## templates 폴더에서 
todo/templates/todo/todo_list.html처럼 앱 이름과 같은 폴더를 한 번 더 만들어주는 게 권장되는 방식
Django는 templates/ 폴더 아래를 전체 템플릿 경로로 인식하기 때문에 모든 앱이 templates/만 쓰면 파일명이 겹침
그래서 "앱 이름"으로 하위 폴더를 한 번 더 만들어주는 것이 좋음
=> templates/앱이름/파일.html 방식은 Django의 템플릿 충돌 방지를 위한 관례적인 구조


## URL → View → HTML 
URL → View → HTML 순서로 진행한 이유는 Django의 MTV(Model-Template-View) 패턴과 연관이 있음
    URL을 먼저 만들면, 프로젝트 구조가 명확해짐
    뷰 함수를 만들면서 URL이 이미 정해져 있으니, 연결만 하면 됨
    디버깅이 쉬워짐

    뷰는 "이 URL에서 어떤 동작을 할 것인지" 결정하는 단계
    URL을 정해두면 뷰에서 어떤 데이터를 다룰지 명확해짐
    HTML을 만들기 전에, 필요한 데이터를 먼저 처리

    HTML(템플릿)은 마지막에 만드는 이유
    뷰에서 보낸 데이터를 출력할 준비가 끝나야 템플릿을 만들 수 있음
    템플릿을 만들 때, 기능이 확실해져서 불필요한 코드가 줄어듦



## 

todo/urls.py에서 path("", todo_list, name="todo_list"),  
왜 todo_list.views라고 하지 않고 todo_list라고만 했을까?

    - from .views import todo_list
    이건 현재 앱(todo) 안의 views.py에서 todo_list 함수를 불러온다는 뜻
    앞에 .은 현재 디렉토리(=todo 앱)를 의미함
    이 방식은 깔끔하고, 앱이름이 바뀌어도 수정할 게 적어서 유리함

    - from todo.views import todo_list
    이건 앱 이름을 명시적으로 지정하는 방식
    프로젝트 규모가 커져서 앱이 여러 개 있을 때는 이렇게 써주는 게 가독성에 도움이 될 수도 있음
    단점은 나중에 앱 이름이 바뀌면 이걸 다 찾아서 바꿔야 함


## is_valid() 사용하려고 했는데 오류 남
    📌 전에 is_valid()를 사용했던 경우
        ✔ Django의 Form 또는 ModelForm을 사용할 때만 is_valid()를 쓸 수 있음!
        ✔ is_valid()는 폼 데이터가 유효한지 검증하는 메서드
        ✔ 예전에 사용했던 is_valid()는 Django의 forms.py에서 정의한 폼 객체에서 쓴 거야!

    📌 하지만 지금은?
        ✔ 우리는 그냥 request.POST를 바로 가져와서 처리하고 있음
        ✔ request.POST는 단순한 QueryDict 객체라서 is_valid()가 없음!
        ✔ 그래서 is_valid()를 쓰려면 Django의 Form을 먼저 만들어야 함!

    📌 todo/forms.py
    from django import forms
    from .models import Todo

    class TodoForm(forms.ModelForm):  # ✅ ModelForm을 사용
        class Meta:
            model = Todo
            fields = ["title"]  # ✅ title 필드만 사용

    추가하면 is_valid() 사용 가능 / 일단 사용하진 않겠음