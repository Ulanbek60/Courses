from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'about', AboutViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'course-reviews', CourseReviewViewSet)
router.register(r'teacher-reviews', TeacherReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
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
]
