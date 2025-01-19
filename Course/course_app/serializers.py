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
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'status','category']


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name',]


class CategoryDetailSerializer(serializers.ModelSerializer):
    course_category = CourseListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'course_category']



class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'video',]


class LessonDetailSerializer(serializers.ModelSerializer):
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
        fields = ['title',]

class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date',]

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'description', 'course', 'passing_score', 'duration']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option', 'text', 'test']

class QuestionsSerializer(serializers.ModelSerializer):
    option_questions = OptionSerializer(read_only=True, many=True)
    class Meta:
        model = Questions
        fields = ['questions', 'option_questions']


class ExamStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStudent
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
        fields = ['title', 'course']

class ExamDetailSerializer(serializers.ModelSerializer):
    questions_exam = QuestionsSerializer(read_only=True, many=True)
    class Meta:
        model = Exam
        fields = ['title', 'description', 'course', 'passing_score', 'duration', 'questions_exam', ]

class StudentSerializer(serializers.ModelSerializer):
    certificate_student = CertificateListSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'status', 'email', 'phone_number', 'profile_image', 'certificate_student']

class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username']

class CourseReviewListSerializer(serializers.ModelSerializer):
    student = StudentNameSerializer(read_only=True,)
    created_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')
    class Meta:
        model = CourseReview
        fields = ['student', 'text', 'stars','created_date']


class CourseDetailSerializer(serializers.ModelSerializer):
    course_lesson = LessonListSerializer(many=True, read_only=True)
    course_assignment = AssignmentSerializer(many=True, read_only=True)
    created_at=serializers.DateTimeField(format='%d-%m-%Y  %H:%M')
    course_exam = ExamListSerializer(read_only=True, many=True)
    created_by = TeacherSerializer(read_only=True)
    category=CategorySerializer(read_only=True, many=True)
    reviews_course = CourseReviewListSerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level', 'price', 'created_by', 'created_at', 'updated_at',
                  'certificate_course', 'course_lesson',
                  'course_assignment','course_exam','created_by','reviews_course']

class CourseReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class TeacherReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherReview
        fields = '__all__'

class TeacherReviewListSerializer(serializers.ModelSerializer):
    student = StudentNameSerializer(read_only=True)
    teacher = TeacherNameSerializer(read_only=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = TeacherReview
        fields = ['id', 'student', 'teacher','text', 'stars', 'created_date',]

class TeacherDetailSerializer(serializers.ModelSerializer):
    teacher_about = AboutSerializer(many=True, read_only=True)
    course_teacher = CourseListSerializer(many=True, read_only=True)
    reviews_teacher = TeacherReviewListSerializer(read_only=True, many=True)
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'status', 'experience', 'about_teacher',
                  'specialization', 'course_teacher',  'teacher_about', 'reviews_teacher']

class CourseReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'



