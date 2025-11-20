from django.db import models


class Course(models.Model):
    COURSE_CHOICES = [
        ("1_uz", "1-kurs"),
        ("1_ru", "1 курс"),
        ("2_uz", "2-kurs"),
        ("2_ru", "2 курс"),
        ("3_uz", "3-kurs"),
        ("3_ru", "3 курс"),
        ("4_uz", "4-kurs"),
        ("4_ru", "4 курс"),
    ]

    name = models.CharField(max_length=50, choices=COURSE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()



class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # KI23-09 kabi

    def __str__(self):
        return f"{self.name} → {self.course.get_name_display()}"



class Lesson(models.Model):

    TIME_CHOICES = [
        ("1", "08:30–09:50"),
        ("2", "10:00–11:20"),
        ("3", "11:30–12:50"),
        ("4", "13:00–14:20"),
        ("5", "14:30–15:50"),
        ("6", "16:00–17:20"),
    ]

    WEEK_DAY = [
        ('du', 'Dushanba'),
        ('se', 'Seshanba'),
        ('ch', 'Chorshanba'),
        ('pa', 'Payshanba'),
        ('ju', 'Juma'),
        ('sh', 'Shanba'),
    ]

    WEEK_TYPE = [
        ('all', 'Har hafta'),
        ('even', 'Juft'),
        ('odd', 'Toq'),
    ]

    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    name = models.CharField(max_length=256)   # Fan nomi
    teacher = models.CharField(max_length=255)
    room = models.CharField(max_length=20)

    weekday = models.CharField(max_length=10, choices=WEEK_DAY)
    time_pair = models.CharField(max_length=2, choices=TIME_CHOICES)
    week_type = models.CharField(max_length=10, choices=WEEK_TYPE, default='all')

    def __str__(self):
        return f"({self.group}-> ({self.name} {self.week_type}))"