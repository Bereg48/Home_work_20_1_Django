# Generated by Django 4.2.3 on 2023-07-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_blogentry_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_views',
            field=models.IntegerField(default=0, verbose_name=' number_views'),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='number_views',
            field=models.IntegerField(default=0, verbose_name=' number_views'),
        ),
    ]
