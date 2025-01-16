from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    'student', 'student',
    'teacher', 'teacher',
)

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    profile_image = models.ImageField(upload_to='profiles/')
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(UserProfile):
    status = models.ForeignKey(UserProfile, choices=STATUS_CHOICES,
                               default='student', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status}'


class Teacher(UserProfile):
    status = models.ForeignKey(UserProfile, choices=STATUS_CHOICES,
                               default='teacher', on_delete=models.CASCADE)
    experience = models.CharField(max_length=64)
    about_teacher = models.TextField()
    specialization = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.status}'


class About(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    social_network = models.URLField(null=True, blank=True)
    graduate = models.ImageField(upload_to='graduate_images/')

    def __str__(self):
        return f'{self.teacher} -- {self.social_network}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.category_name}'


