from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('experience', 'about_teacher', 'specialization')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('questions',)


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('text',)


