# Generated by Django 3.0 on 2021-07-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20210730_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emp_salary',
            field=models.FloatField(default=0.0, max_length=30, verbose_name='Amount(₦)'),
        ),
    ]