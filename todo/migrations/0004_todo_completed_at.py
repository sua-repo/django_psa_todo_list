# Generated by Django 4.2.21 on 2025-07-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_todo_important"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="completed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
