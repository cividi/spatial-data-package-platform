# Generated by Django 3.1.14 on 2022-04-14 20:20

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0050_auto_20220414_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='categories',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='gsmap.Category'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='states',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='gsmap.State'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='usergroups',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='gsmap.Usergroup'),
        ),
    ]