# Generated by Django 4.1.2 on 2022-10-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
