# Generated by Django 3.1.5 on 2021-06-09 19:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_auto_20210609_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]