# Generated by Django 3.1.5 on 2021-05-08 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_auto_20210508_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundingrequisition',
            old_name='timestamp',
            new_name='date',
        ),
    ]
