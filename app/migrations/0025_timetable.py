# Generated by Django 5.0.3 on 2024-07-03 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_staff_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/img')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.session')),
            ],
        ),
    ]
