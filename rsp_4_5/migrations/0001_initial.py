# Generated by Django 4.1.1 on 2022-10-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adepa_Base_Nustyle_Safoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drying_temperature', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('speed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('base_colour_misfit', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('selvedge_effect', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('white_patches', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('color_marking_off', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('other_defect', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OWS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatures_washing', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('units_squeezing_pressures', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Steamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('speed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
