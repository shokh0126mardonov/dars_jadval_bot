from django.urls import path
from django.views import View

from .views import GroupCreate,LessonCreate

urlpatterns = [
    path('add_group/',GroupCreate.as_view(), name = 'group_page'),
    path('add_lesson/',LessonCreate.as_view(), name = 'lesson_page'),
]
