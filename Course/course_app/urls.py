from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'course-reviews', CourseReviewViewSet)
router.register(r'teacher-reviews', TeacherReviewViewSet)

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
]
