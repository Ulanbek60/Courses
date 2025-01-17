from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, StudentViewSet, TeacherViewSet, AboutViewSet, CategoryViewSet, CourseViewSet, LessonViewSet, AssignmentViewSet, ExamViewSet, QuestionsViewSet, OptionViewSet, CertificateViewSet, CartViewSet, CartItemViewSet, CourseReviewViewSet, TeacherReviewViewSet

router = DefaultRouter()
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
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'course-reviews', CourseReviewViewSet)
router.register(r'teacher-reviews', TeacherReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
