from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'questions', QuestionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),

    path('student/', StudentAPIView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentDetailUpdateDestroyApiView.as_view(), name='student_detail'),

    path('teacher/', TeacherAPIView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailUpdateDestroyApiView.as_view(), name='teacher_detail'),

    path('about/', AboutListAPIView.as_view(), name='about_detail'),
    path('about/<int:pk>/', AboutRetrieveUpdateDestroyAPIView.as_view(), name='about_detail'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course_list/', CourseAPIView.as_view(), name='course_list'),
    path('course_list/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course_edit'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson'),
    path('lesson/create/', LessonCreateViewSet.as_view(), name='lesson_create'),
    path('lesson_list/', LessonAPIView.as_view(), name='lesson_list'),
    path('lesson_list/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson_list_edit'),
    path('assignment/', AssignmentListAPIView.as_view(), name='assignment'),
    path('assignment/create/', AssignmentCreateAPIView.as_view(), name='assignment_create'),
    path('assignment_list/', AssignmentAPIView.as_view(), name='assignment_list'),
    path('assignment_list/<int:pk>/', AssignmentRetrieveUpdateDestroyAPIView.as_view(), name='assignment_list_edit'),
    path('exam/', ExamListViewSet.as_view(), name='exam'),
    path('exam/create/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('exam_list/', ExamViewSet.as_view(), name='exam_list'),
    path('exam_list/<int:pk>/', ExamRetrieveUpdateDestroyAPIView.as_view(), name='exam_list_edit'),
    path('certificates/', CertificateListAPIView.as_view(), name='certificate_list'),
    path('certificates/create/', CertificateCreateAPIView.as_view(), name='certificates_create'),
    path('carts/', CartListAPIView.as_view(), name='cart_list'),
    path('carts/<int:pk>/', CartItemDerailAPiView.as_view(), name='cart_item_detail'),
    path('reviews/', CourseReviewListAPIView.as_view(), name='review_list'),
    path('review/create/', CourseReviewCreateAPIView.as_view(), name='review_create'),
    path('teacher_reviews/', TeacherReviewListAPIView.as_view(), name='teacher_review_list'),
    path('teacher_reviews/<int:pk>/', TeacherReviewDetailUpdateDestroyAPIView.as_view(), name='teacher_review_detail'),
    path('teacher_reviews/create/', TeacherReviewCreateAPIView.as_view(), name='teacher_review_create'),

]
