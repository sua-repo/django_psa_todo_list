from django.db import models

# Create your models here.

class Todo(models.Model) : 
    title = models.CharField(max_length=255)    # todo 제목
    is_completed = models.BooleanField(default=False)   # todo 완료 여부
    
    created_at = models.DateTimeField(auto_now_add=True)    # todo 생성 날짜 (객체가 처음 생성될 때만 현재 시간이 저장)
    # updated_at = models.DateTimeField(auto_now=True)    # todo 수정 날짜 (객체가 수정될 때마다 현재 시간이 저장)
    # created_at은 생성 시각을 저장하고, updated_at을 추가하면 수정된 시간도 추적할 수 있음

    important = models.BooleanField(default=False)  # 중요 표시 필드 추가
    
    completed_at = models.DateTimeField(null=True, blank=True)  # 자동 삭제 기준이 되는 완료 날짜 필드 추가

    def __str__(self) :
        return self.title   # 관리자 페이지에서 객체를 제목으로 표시
