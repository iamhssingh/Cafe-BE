# Generated by Django 2.1 on 2018-09-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Section')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Display Section',
                'verbose_name_plural': 'Display Sections',
            },
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=254, unique=True, verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='item',
            name='sections',
            field=models.ManyToManyField(to='restaurant.Section'),
        ),
    ]
