# Generated by Django 3.1.4 on 2022-02-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220208_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField()),
                ('ans', models.TextField()),
            ],
        ),
    ]
