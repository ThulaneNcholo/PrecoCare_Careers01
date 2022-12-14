# Generated by Django 4.1 on 2022-08-26 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PrecoCareCareers', '0004_agentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joblisting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=300, null=True)),
                ('company', models.CharField(max_length=300, null=True)),
                ('city', models.CharField(max_length=300, null=True)),
                ('province', models.CharField(max_length=300, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('mon_fri', models.CharField(max_length=300, null=True)),
                ('saturdays', models.CharField(max_length=300, null=True)),
                ('sundays', models.CharField(max_length=300, null=True)),
                ('holidays', models.CharField(max_length=300, null=True)),
                ('job_status', models.CharField(max_length=300, null=True)),
                ('contact_lenght', models.CharField(max_length=300, null=True)),
                ('salary', models.CharField(max_length=300, null=True)),
                ('open_positions', models.IntegerField(blank=True, null=True)),
                ('requirements_1', models.TextField(blank=True, null=True)),
                ('requirements_2', models.TextField(blank=True, null=True)),
                ('requirements_3', models.TextField(blank=True, null=True)),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('application_status', models.CharField(default='Open', max_length=300, null=True)),
                ('views', models.IntegerField(blank=True, null=True)),
                ('paid_promo', models.CharField(default='No', max_length=300, null=True)),
                ('User', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('agent', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='PrecoCareCareers.agentmodel')),
            ],
        ),
    ]
