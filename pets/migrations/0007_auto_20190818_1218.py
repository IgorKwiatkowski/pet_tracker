# Generated by Django 2.2.4 on 2019-08-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_auto_20190818_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosage',
            name='date_added',
            field=models.DateField(verbose_name='Od kiedy'),
        ),
    ]
