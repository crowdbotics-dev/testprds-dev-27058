# Generated by Django 2.2.28 on 2022-09-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.BigIntegerField()),
            ],
        ),
    ]
