# Generated by Django 2.2.4 on 2019-08-18 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_auto_20190818_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosage',
            name='date_added',
            field=models.DateField(default=datetime.date(2019, 8, 18), verbose_name='Od kiedy'),
        ),
    ]