from django.contrib import admin
from .models import (
    UserProfile, Student, Teacher, About, Category, Course, Lesson,
    Assignment, Exam, Questions, Option, Certificate, Cart,
    CartItem, CourseReview, TeacherReview
)

class LessonInLine(admin.TabularInline):
    model = Lesson
    extra = 1

class AssignmentInLine(admin.TabularInline):
    model = Assignment
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInLine,AssignmentInLine]

class OptionInLine(admin.TabularInline):
    model = Option
    extra = 1

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    inlines = [OptionInLine]


admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(Option)
admin.site.register(Certificate)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CourseReview)
admin.site.register(TeacherReview)

