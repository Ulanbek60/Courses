from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username','first_name', 'last_name', 'email', 'phone_number', 'profile_image']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=Teacher.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=Student.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LoginSerializers(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, data):
        user=authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh=RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError({'detail': 'Недействительный или уже отозванный токен'})


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True, many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    get_good_check = serializers.SerializerMethodField()
    get_discount_price = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['course_name','category', 'level', 'price', 'created_by', 'get_avg_rating',
                  'get_count_people', 'get_good_check', 'get_discount_price']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_people(self,obj):
        return obj.get_count_people()

    def get_good_check(self,obj):
        return obj.get_good_check()

    def get_discount_price(self,obj):
        return obj.get_discount_price()


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['teacher_about', 'social_network', 'graduate']


class TeacherSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'status','category']


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


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

class OptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    option_questions = OptionSerializer(read_only=True, many=True)
    class Meta:
        model = Questions
        fields = ['questions', 'option_questions']


class QuestionsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class ExamStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStudent
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
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


class CartListSerializer(serializers.ModelSerializer):
    user = StudentNameSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['user', 'created_date']

class CartItemDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    cart = CartListSerializer(read_only=True)
    get_total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['cart', 'course', 'quantity', 'get_total_price']

    def get_total_price(self,obj):
        return obj.get_total_price()



