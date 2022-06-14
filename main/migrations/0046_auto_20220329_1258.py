# Generated by Django 3.1.4 on 2022-03-29 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0045_auto_20220329_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainertask',
            name='trainer_ts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_ts', to='main.trainer'),
        ),
        migrations.AlterField(
            model_name='trainertask',
            name='user_ts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_ts', to=settings.AUTH_USER_MODEL),
        ),
    ]