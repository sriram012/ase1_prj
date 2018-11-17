# Generated by Django 2.1.2 on 2018-11-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_question_no_of_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], default='0', max_length=5, verbose_name='Difficulty level'),
        ),
        migrations.AlterField(
            model_name='question',
            name='no_of_views',
            field=models.IntegerField(default=0, null=True, verbose_name='Views count'),
        ),
    ]
