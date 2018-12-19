# Generated by Django 2.1.4 on 2018-12-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suborder',
            name='uom',
            field=models.CharField(choices=[('G', 'Grams'), ('KG', 'Kilo Grams'), ('PLT', 'Plates'), ('L', 'Litres'), ('ML', 'Milli Litres'), ('M', 'Meters'), ('KM', 'Kilo Meters'), ('MM', 'Milli Meters'), ('GLS', 'Glasses'), ('CP', 'Cups')], default='PLT', max_length=15, verbose_name='Unit of Measurement'),
        ),
    ]
