from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


STATUS_CHOICES = (
    ('student', 'student'),
    ('teacher', 'teacher'),
)

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    profile_image = models.ImageField(upload_to='profiles/')
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(UserProfile):
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='student')

    class Meta:
        verbose_name_plural = "Student"

    def __str__(self):
        return f'{self.status} {self.username}'


class Teacher(UserProfile):
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='teacher')
    experience = models.CharField(max_length=64)
    about_teacher = models.TextField()
    specialization = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Teacher"

    def __str__(self):
        return f'{self.status}'

class About(models.Model):
    teacher_about = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_about')
    social_network = models.URLField(null=True, blank=True)
    graduate = models.ImageField(upload_to='graduate_images/')

    def __str__(self):
        return f'{self.teacher_about} -- {self.social_network}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    LEVEL_CHOICES_COURSE = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES_COURSE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    STATUS_CERTIFICATE_CHOICES = (
        ('Сертификат об окончании', 'Сертификат об окончании'),
        ('Не дается сертификат', 'Не дается сертификат'),
    )
    certificate_course = models.CharField(max_length=100, choices=STATUS_CERTIFICATE_CHOICES)


    def __str__(self):
        return f'{self.course_name}'


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField(null=True, blank=True)
    duration = models.DurationField()

    def __str__(self):
        return f'{self.title}'


class Questions(models.Model):
    questions = models.CharField(max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.questions}'


class Option(models.Model):
    option = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    test = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.option}'


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return f'{self.student} -- {self.course}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    def str(self):
        return f'{self.course} -- {self.quantity}'


class CourseReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews_course')
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='рейтинг')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, - {self.stars}'


class TeacherReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='reviews_teacher')
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='рейтинг')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, - {self.stars}'
