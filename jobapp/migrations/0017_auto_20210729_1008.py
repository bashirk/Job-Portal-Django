# Generated by Django 3.0 on 2021-07-29 10:08

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('jobapp', '0016_auto_20210727_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='jobapp.Category'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(blank=True, choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
