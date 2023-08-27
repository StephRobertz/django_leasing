# Generated by Django 4.2.4 on 2023-08-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='carname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='gear',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='customer',
            name='adress',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customername',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mail',
            field=models.CharField(default=30, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(default='Finland', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='postalcode',
            field=models.CharField(default='', max_length=50),
        ),
    ]