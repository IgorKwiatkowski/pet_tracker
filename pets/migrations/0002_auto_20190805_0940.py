# Generated by Django 2.2.4 on 2019-08-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pets',
            field=models.ManyToManyField(through='pets.Dosage', to='pets.Pet', verbose_name='Zwierzę'),
        ),
    ]
