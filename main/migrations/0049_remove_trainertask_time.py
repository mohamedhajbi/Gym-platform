# Generated by Django 3.1.4 on 2022-03-29 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_trainertask_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainertask',
            name='time',
        ),
    ]