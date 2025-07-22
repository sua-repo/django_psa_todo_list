from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('/todo/')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', root_redirect),
    # 'todo/' 경로로 들어오면 todo.urls에서 처리하도록 연결
    path("todo/", include("todo.urls")),    # dev_2
    
]
