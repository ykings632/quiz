# Generated by Django 2.2.4 on 2019-09-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdmanage', '0004_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='result_exam_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
