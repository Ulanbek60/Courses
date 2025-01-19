from rest_framework import viewsets, generics
from .permissions import CheckEditTeacher, CheckStatusCreate, CheckStudentReview
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filter import CourseFilter
from .paginations import CourseResultSetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(id=self.request.user.id)


class StudentDetailUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get_queryset(self):
        return Student.objects.filter(id=self.request.user.id)


class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer


class AboutListAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [CheckEditTeacher]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filterset_class = CourseFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['course_name']
    pagination_class = CourseResultSetPagination
    ordering_fields = ['price']


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer
    permission_classes = [CheckStatusCreate]


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [CheckEditTeacher]


class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

    def get_queryset(self):
        return Course.objects.filter(id=self.request.user.id)

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer

class LessonCreateViewSet(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [CheckStatusCreate]


class LessonAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [CheckEditTeacher]


class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer

class AssignmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AssignmentListSerializer
    permission_classes = [CheckStatusCreate]


class AssignmentAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer
    permission_classes = [CheckEditTeacher]


class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer

class ExamRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer

class ExamCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamSerializer
    permission_classes = [CheckStatusCreate]

class ExamViewSet(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer


class ExamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [CheckEditTeacher]


class QuestionsListAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class QuestionsCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionsCreateUpdateSerializer
    permission_classes = [CheckStatusCreate]

class OptionListAPIView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class OptionCreateAPIView(generics.CreateAPIView):
    serializer_class = OptionCreateSerializer
    permission_classes = [CheckStatusCreate]

class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer

class CertificateCreateAPIView(generics.CreateAPIView):
    serializer_class = CertificateSerializer
    permission_classes = [CheckStatusCreate]


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Cart.objects.filter(id=self.request.user.id)

class CartItemDetailAPiView(generics.RetrieveDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return CartItem.objects.filter(id=self.request.user.id)

class CourseReviewListAPIView(generics.ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer
    permission_classes = [CheckEditTeacher]


class CourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TeacherReviewListAPIView(generics.ListAPIView):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewListSerializer


class TeacherReviewDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewCreateSerializer


class TeacherReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = TeacherReviewCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckStudentReview]


class TeacherProfileListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherProfileSerializer

    def get_queryset(self):
        return Teacher.objects.filter(id=self.request.user.id)


class TeacherProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherProfileSerializer

    def get_queryset(self):
        return Teacher.objects.filter(id=self.request.user.id)


class ExamStudentCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamStudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckStudentReview]
