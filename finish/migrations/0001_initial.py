# Generated by Django 4.1.1 on 2022-10-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baking_Oven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loop', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('spread', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('residence_time', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('temperature', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eveness_of_shiny_effect', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('temperature', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('speed_fancy_woodin_dumas', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stenter_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('straightness_of_design', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('straightness_of_fibre', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('moisture_outfeed_cloth_with', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stenter_7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('straightness_of_design', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('straightness_of_fibre', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('moisture_outfeed_cloth_with', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
