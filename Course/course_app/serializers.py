from rest_framework import serializers
from .models import Student, Teacher, About, Category, Course, Lesson, Assignment, Exam, Questions, Option, Certificate, Cart, CartItem, CourseReview, TeacherReview


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']


class StudentSerializer(serializers.ModelSerializer):
    certificate_student = CertificateListSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'status', 'email', 'phone_number', 'profile_image', 'certificate_student']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['teacher_about', 'social_network', 'graduate']


class TeacherSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    course_teacher = CourseSerializer(many=True, read_only=True)
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
    course_category = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'course_category']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'

class TeacherReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherReview
        fields = '__all__'
