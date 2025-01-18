from rest_framework import viewsets, generics
from .serializers import *


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer


class AboutListAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer


class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

class CourseDetailAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonCreateViewSet(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AssignmentListSerializer


class AssignmentAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer

class ExamListViewSet(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer

class ExamCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamSerializer

class ExamViewSet(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer


class ExamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer


class CertificateCreateAPIView(generics.CreateAPIView):
    serializer_class = CertificateSerializer


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer

class CartItemDerailAPiView(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer

class CourseReviewListAPIView(generics.ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer


class CourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewCreateSerializer


class TeacherReviewListAPIView(generics.ListAPIView):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewListSerializer


class TeacherReviewDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewListSerializer


class TeacherReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = TeacherReviewCreateSerializer