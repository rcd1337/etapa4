# Generated by Django 3.1.5 on 2021-01-29 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradesmanager', '0002_auto_20210129_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prova',
            name='nota',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]