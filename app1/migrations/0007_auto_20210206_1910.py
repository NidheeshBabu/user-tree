# Generated by Django 3.1.2 on 2021-02-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_tbl_user_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_user',
            name='currentPoints',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_user',
            name='userImage',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
