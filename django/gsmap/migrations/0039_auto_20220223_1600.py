# Generated by Django 3.1.13 on 2022-02-23 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0038_migrate_translatable_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='_description',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='_title',
        ),
    ]