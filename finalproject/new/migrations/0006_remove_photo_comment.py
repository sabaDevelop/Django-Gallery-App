# Generated by Django 4.2.4 on 2023-09-03 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0005_alter_photo_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='comment',
        ),
    ]