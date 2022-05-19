# Generated by Django 3.1.14 on 2022-05-19 14:23

from django.db import migrations, models
import gsmap.models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0055_auto_20220501_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='permission',
            field=models.IntegerField(choices=[(0, 'PUBLIC'), (10, 'NOT_LISTED'), (20, 'PRIVATE')], default=gsmap.models.WorkspacePermission['PRIVATE']),
        ),
    ]