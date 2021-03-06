# Generated by Django 3.1.4 on 2020-12-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_enabled', models.BooleanField(default=True)),
                ('homepage_snippet', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
