# Generated by Django 3.1.4 on 2022-02-08 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_pages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pages',
            new_name='Page',
        ),
    ]