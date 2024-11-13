# Generated by Django 5.1.2 on 2024-11-13 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_lesson_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSpecial',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.course')),
                ('limit_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('courses.course',),
        ),
    ]