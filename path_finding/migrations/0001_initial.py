# Generated by Django 4.0.8 on 2025-01-08 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_user_date_of_birth_user_enrollment_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'ordering': ['-date_taken'],
            },
        ),
        migrations.CreateModel(
            name='TestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.PositiveIntegerField()),
                ('answer_text', models.TextField()),
                ('test_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_answers', to='path_finding.testsession')),
            ],
        ),
    ]