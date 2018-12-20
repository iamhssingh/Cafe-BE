# Generated by Django 2.1.4 on 2018-12-20 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20181219_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='managed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='outlet.OutletManager', verbose_name='Outlet Manager'),
        ),
    ]
