# Generated by Django 3.1.14 on 2022-04-20 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0047_auto_20220406_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytranslation',
            name='help_text',
            field=models.TextField(blank=True, default='', verbose_name='help_text'),
        ),
    ]