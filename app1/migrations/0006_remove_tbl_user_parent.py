# Generated by Django 3.1.2 on 2021-02-06 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210206_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_user',
            name='parent',
        ),
    ]
