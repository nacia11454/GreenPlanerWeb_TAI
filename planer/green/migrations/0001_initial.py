# Generated by Django 4.0.5 on 2022-06-22 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreenUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=100, verbose_name='Plant Name')),
                ('plant_photo', models.URLField(verbose_name='Plant Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Plant_species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_species', models.CharField(max_length=100, verbose_name='Species Name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100, verbose_name='Task Title')),
                ('task_date', models.DateTimeField(verbose_name='Task Date')),
                ('task_note', models.TextField(blank=True)),
                ('task_status', models.IntegerField(default=0)),
                ('task_plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='green.plant')),
                ('task_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='green.greenuser')),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='green.plant_species'),
        ),
    ]
