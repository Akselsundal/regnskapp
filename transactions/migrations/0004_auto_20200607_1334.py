# Generated by Django 3.0.6 on 2020-06-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20200605_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='happy',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', 1), ('2', 2), ('3', 3)], null=True),
        ),
    ]
