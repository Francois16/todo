# Generated by Django 4.0 on 2021-12-26 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todocategory_todo_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoCategory',
            new_name='Category',
        ),
    ]
