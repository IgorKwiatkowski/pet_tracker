# Generated by Django 2.2.4 on 2019-08-05 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20190805_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosage',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]