# Generated by Django 3.1.5 on 2021-06-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210607_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='transaction_number',
            field=models.PositiveIntegerField(blank=True, help_text='Παρακαλώ εισάγετε τον 9ψήφιο κωδικό συναλλαγής', unique=True),
        ),
    ]