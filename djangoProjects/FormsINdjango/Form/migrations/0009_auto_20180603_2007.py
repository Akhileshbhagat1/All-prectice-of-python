# Generated by Django 2.0.3 on 2018-06-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0008_auto_20180603_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default='1-1-2019'),
        ),
    ]