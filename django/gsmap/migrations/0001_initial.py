# Generated by Django 3.0.2 on 2020-01-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('canton', models.CharField(choices=[('GR', 'Graubünden'), ('GL', 'Glarus'), ('VD', 'Vaud'), ('VS', 'Valais'), ('BE', 'Bern'), ('TI', 'Ticino'), ('SZ', 'Schwyz'), ('UR', 'Uri'), ('SG', 'St. Gallen'), ('NE', 'Neuchâtel'), ('TG', 'Thurgau'), ('FR', 'Fribourg'), ('LU', 'Luzern'), ('NW', 'Nidwalden'), ('OW', 'Obwalden'), ('ZH', 'Zürich'), ('JU', 'Jura'), ('AI', 'Appenzell Innerrhoden'), ('AR', 'Appenzell Ausserrhoden'), ('SH', 'Schaffhausen'), ('ZG', 'Zug'), ('SO', 'Solothurn'), ('BS', 'Basel-Stadt'), ('AG', 'Aargau'), ('GE', 'Genève'), ('BL', 'Basel-Landschaft')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'municipalities',
            },
        ),
    ]
