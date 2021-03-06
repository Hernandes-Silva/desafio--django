# Generated by Django 4.0 on 2022-04-23 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_question', to='quiz.question')),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(related_name='quiz', to='quiz.QuizQuestion'),
        ),
    ]
