# Generated by Django 3.1.4 on 2022-02-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='pwd',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]