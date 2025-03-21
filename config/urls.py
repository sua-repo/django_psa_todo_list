from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # 'todo/' 경로로 들어오면 todo.urls에서 처리하도록 연결
    path("todo/", include("todo.urls")),    # dev_2
]
