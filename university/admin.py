from django.contrib import admin
from .models import Teacher, Student, Question, Choice, Quiz, Class  #Image,

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'avg_mark')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('title',)

# @admin.register(A)
# class AAdmin(admin.ModelAdmin):
#     list_display = ('text_a',)
#
# @admin.register(B)
# class BAdmin(admin.ModelAdmin):
#     list_display = ('text_b',)