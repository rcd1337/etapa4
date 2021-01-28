# Generated by Django 3.1.5 on 2021-01-28 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('aprovado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Gabarito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gabarito', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respostas', models.TextField()),
                ('nota', models.DecimalField(decimal_places=1, max_digits=3)),
                ('aluno_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gradesmanager.aluno')),
                ('gabarito_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gradesmanager.gabarito')),
            ],
        ),
    ]
