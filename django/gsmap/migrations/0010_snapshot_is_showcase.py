# Generated by Django 3.0.3 on 2020-03-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0009_auto_20200306_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshot',
            name='is_showcase',
            field=models.BooleanField(default=False),
        ),
    ]