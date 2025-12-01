import json

from django.http import JsonResponse,HttpRequest
from django.views import View

from .models import Group,Course,Lesson

class GroupCreate(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        try:
            data_list = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Invalid JSON: {str(e)}'}, status=400)

        created_groups = []
        skipped_groups = []

        for data in data_list:
            name = data.get('name')
            course_name = data.get('course')  # requestdan keladi

            if not name:
                return JsonResponse({'name': 'Required'}, status=400)

            # course bo'lmasa default
            if not course_name:
                course = Course.objects.first()
                if not course:
                    course = Course.objects.create(name="1")
            else:
                course, _ = Course.objects.get_or_create(name=course_name)

            # Dublikat tekshirish
            group, created = Group.objects.get_or_create(
                name=name,
                course=course
            )

            if created:
                created_groups.append({'name': group.name, 'course': course.get_name_display()})
            else:
                skipped_groups.append({'name': group.name, 'course': course.get_name_display()})

        return JsonResponse({
            'created_groups': created_groups,
            'skipped_groups': skipped_groups
        })

    
class LessonCreate(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        try:
            lessons_data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Invalid JSON: {str(e)}'}, status=400)

        created_lessons = []
        skipped_lessons = []

        for data in lessons_data:
            name = data.get('name')
            room = data.get('room')
            teacher = data.get('teacher')
            time_pair = data.get('time_pair')
            weekday = data.get('weekday')
            week_type = data.get('week_type', 'all')
            group_name = data.get('group')
            course_name = data.get('course')

            if not all([name, room, teacher, time_pair, weekday, group_name]):
                return JsonResponse({'error': 'Missing required field'}, status=400)

            # course tayyorlash
            if not course_name:
                course = Course.objects.first()
                if not course:
                    course = Course.objects.create(name="1")
            else:
                course, _ = Course.objects.get_or_create(name=course_name)

            # group tayyorlash
            group, _ = Group.objects.get_or_create(name=group_name, defaults={'course': course})

            # Dublikat lesson tekshirish
            lesson, created = Lesson.objects.get_or_create(
                name=name,
                room=room,
                teacher=teacher,
                time_pair=time_pair,
                weekday=weekday,
                week_type=week_type,
                group=group
            )

            if created:
                created_lessons.append({
                    'name': name,
                    'group': group_name,
                    'room': room,
                    'teacher': teacher,
                    'time_pair': time_pair,
                    'weekday': weekday,
                    'week_type': week_type
                })
            else:
                skipped_lessons.append({
                    'name': name,
                    'group': group_name,
                    'room': room,
                    'teacher': teacher,
                    'time_pair': time_pair,
                    'weekday': weekday,
                    'week_type': week_type
                })

        return JsonResponse({
            'created_lessons': created_lessons,
            'skipped_lessons': skipped_lessons
        })
