# Generated by Django 4.2.3 on 2023-08-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_version_name_current_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='name_current_version',
            field=models.BooleanField(default=True, verbose_name='признак текущей версии'),
        ),
    ]
