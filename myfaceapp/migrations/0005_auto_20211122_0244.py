# Generated by Django 3.0.14 on 2021-11-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfaceapp', '0004_auto_20210710_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]