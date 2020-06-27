# Generated by Django 3.0.7 on 2020-06-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_ques'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='message',
            new_name='ques_description',
        ),
        migrations.AddField(
            model_name='question',
            name='ques_slug',
            field=models.SlugField(null=True),
        ),
    ]
