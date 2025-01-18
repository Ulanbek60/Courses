from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['course_name','category', 'level', 'price', 'created_by',]


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['teacher_about', 'social_network', 'graduate']


class TeacherSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    course_teacher = CourseListSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'status', 'experience', 'about_teacher',
                  'specialization', 'course_teacher', 'category']


class TeacherDetailSerializer(serializers.ModelSerializer):
    teacher_about = AboutSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'status', 'experience', 'about_teacher',
                  'specialization', 'teacher_about']



class CategoryDetailSerializer(serializers.ModelSerializer):
    course_category = CourseListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'course_category']



class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'video', 'content','course']


class CertificateListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    class Meta:
        model = Certificate
        fields = ['course', 'issued_at', 'certificate_url']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'students']

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'description', 'course', 'passing_score', 'duration']

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'



class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class CartListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Cart
        fields = '__all__'

class CartItemDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer( read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    course_lesson = LessonListSerializer(many=True, read_only=True)
    course_assignment = AssignmentSerializer(many=True, read_only=True)
    created_at=serializers.DateTimeField(format='%d-%m-%Y  %H:%M')
    course_exam = ExamListSerializer(read_only=True, many=True)
    created_by = TeacherSerializer(read_only=True)
    category=CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level', 'price', 'created_by', 'created_at', 'updated_at',
                  'certificate_course', 'course_lesson',
                  'course_assignment','course_exam','created_by']


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    certificate_student = CertificateListSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'status', 'email', 'phone_number', 'profile_image', 'certificate_student']

class CourseReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class TeacherReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherReview
        fields = '__all__'

class TeacherReviewListSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = TeacherReview
        fields = ['id', 'teacher', 'stars', 'created_date', 'student']

class CourseReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


