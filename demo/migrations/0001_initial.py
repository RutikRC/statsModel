# Generated by Django 5.0.1 on 2024-01-17 06:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='stepsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[('project_start', 'Project Start'), ('structural_work', 'Structural Work'), ('laminate_work', 'Laminate Work'), ('hardware_install', 'Hardware Installation'), ('furnishing_work', 'Furnishing Work'), ('hand_over_and_finalizing', 'Hand Over and Finalizing')], default='project_start', max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='imgTitleStructuralWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='structural_work_images/')),
                ('stepsmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.stepsmodel')),
            ],
        ),
    ]
