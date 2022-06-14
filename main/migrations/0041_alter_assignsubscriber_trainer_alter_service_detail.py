# Generated by Django 4.0.3 on 2022-03-22 12:34

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20220309_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubscriber',
            name='trainer',
            field=models.ForeignKey(default='no one', on_delete=django.db.models.deletion.CASCADE, to='main.trainer'),
        ),
        migrations.AlterField(
            model_name='service',
            name='detail',
            field=froala_editor.fields.FroalaField(),
        ),
    ]