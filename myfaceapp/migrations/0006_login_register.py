# Generated by Django 3.0.14 on 2021-11-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfaceapp', '0005_auto_20211122_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lmobile_number', models.IntegerField(max_length=10)),
                ('lpassword', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
