# Generated by Django 3.1.5 on 2021-06-07 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinstallment',
            name='postgrad_year',
            field=models.IntegerField(blank=True, choices=[(2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 7, 21, 26, 18, 316900)),
        ),
    ]
