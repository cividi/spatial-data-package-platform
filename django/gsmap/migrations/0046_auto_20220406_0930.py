# Generated by Django 3.1.14 on 2022-04-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0045_auto_20220314_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='comments_enabled',
            field=models.BooleanField(default=False, verbose_name='comments'),
        ),
    ]
