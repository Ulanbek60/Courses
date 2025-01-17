from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *
router = SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'about', AboutViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'questions', QuestionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
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
