# Generated by Django 3.1.4 on 2022-02-26 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_auto_20220226_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_details', models.TextField()),
                ('status', models.BooleanField()),
                ('read_by_trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
                ('read_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]