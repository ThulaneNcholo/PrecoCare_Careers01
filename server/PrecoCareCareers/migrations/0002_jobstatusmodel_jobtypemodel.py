# Generated by Django 4.1 on 2022-08-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrecoCareCareers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=300, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=300, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
