# Generated by Django 2.2.28 on 2022-09-22 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_tested_yes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tested",
            name="yes",
        ),
    ]