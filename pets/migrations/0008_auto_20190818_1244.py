# Generated by Django 2.2.4 on 2019-08-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20190818_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosage',
            name='notes',
            field=models.TextField(null=True, verbose_name='Uwagi'),
        ),
    ]
