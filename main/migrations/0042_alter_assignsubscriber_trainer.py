# Generated by Django 4.0.3 on 2022-03-22 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_alter_assignsubscriber_trainer_alter_service_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubscriber',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer'),
        ),
    ]