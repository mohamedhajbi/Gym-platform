# Generated by Django 3.1.4 on 2022-03-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_subplan_validity_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='reg_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]