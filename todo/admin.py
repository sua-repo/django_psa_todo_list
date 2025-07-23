from django.contrib import admin

from todo.models import Todo

# Register your models here.

# 관리자 페이지에 등록
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'important', 'completed_at', 'created_at')