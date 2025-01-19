# Generated by Django 5.1.5 on 2025-01-19 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_remove_examstudent_answer_delete_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_questions', to='course_app.questions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_exam', to='course_app.exam'),
        ),
    ]