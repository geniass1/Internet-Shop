# Generated by Django 3.1.5 on 2021-01-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('user', '0002_auto_20210118_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='catalog',
            field=models.ManyToManyField(blank=True, to='main.Product'),
        ),
    ]