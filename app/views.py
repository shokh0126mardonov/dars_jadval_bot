import json

from django.http import JsonResponse,HttpRequest
from django.views import View

from .models import Group,Course

class GroupCreate(View):
    def post(self,request:HttpRequest)->JsonResponse:
  
        for data in json.loads(request.body.decode()):
            name = data.get('name')
            course = data.get('course')

            existing_course = Course.objects.get(name = course)
            if  existing_course is None:
                return JsonResponse({'course':'error'},status = 400)
            
            if name is None:
                return JsonResponse({'name':'Required'})
            
            new_group = Group(name = name,course = existing_course)
            new_group.save()
            

            return JsonResponse({'name':new_group.name})
        

from django.views import View
from django.http import JsonResponse, HttpRequest
from .models import Lesson, Group
import json

class LessonCreate(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        try:
            lessons_data = json.loads(request.body.decode())
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        created_lessons = []

        for data in lessons_data:
            # JSON-dan ma'lumotlarni olish
            name = data.get('name')
            room = data.get('room')
            teacher = data.get('teacher')
            time_pair = data.get('time_pair')
            weekday = data.get('weekday')
            week_type = data.get('week_type', 'all')
            group_name = data.get('group')

            # Majburiy maydonlarni tekshirish
            if not all([name, room, teacher, time_pair, weekday, group_name]):
                return JsonResponse({'error': 'Missing required field'}, status=400)

            # Group obyektini olish
            try:
                group = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                return JsonResponse({'error': f'Group {group_name} not found'}, status=400)

            # Lesson yaratish
            lesson = Lesson.objects.create(
                name=name,
                room=room,
                teacher=teacher,
                time_pair=time_pair,
                weekday=weekday,
                week_type=week_type,
                group=group
            )

            created_lessons.append(lesson.name)

        return JsonResponse({'created_lessons': created_lessons})
