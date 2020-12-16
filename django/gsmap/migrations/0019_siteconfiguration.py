# Generated by Django 3.0.3 on 2020-12-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0018_auto_20200510_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
