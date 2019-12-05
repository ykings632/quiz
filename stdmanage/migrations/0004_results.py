# Generated by Django 2.2.4 on 2019-09-21 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdmanage', '0003_auto_20190914_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_question', models.CharField(max_length=200)),
                ('result_choice1', models.CharField(max_length=100)),
                ('result_choice2', models.CharField(max_length=100)),
                ('result_choice3', models.CharField(max_length=100)),
                ('result_choice4', models.CharField(max_length=100)),
                ('result_correct_answer', models.CharField(max_length=100)),
                ('result_choose_correct', models.CharField(max_length=100)),
                ('result_user_id', models.CharField(max_length=100)),
                ('result_exam_date', models.DateTimeField()),
            ],
        ),
    ]
