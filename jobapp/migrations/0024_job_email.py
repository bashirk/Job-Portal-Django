# Generated by Django 3.0 on 2021-07-31 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0023_taskowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.EmailField(default='admin@workings.ng', error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True),
        ),
    ]