# Generated by Django 4.1 on 2022-08-26 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PrecoCareCareers', '0005_joblisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('doctor_lisence', models.CharField(max_length=200, null=True)),
                ('exp1_titl2', models.CharField(max_length=200, null=True)),
                ('exp1_comp2ny', models.CharField(max_length=200, null=True)),
                ('exp1_numb2r', models.CharField(max_length=20, null=True)),
                ('exp2_title', models.CharField(max_length=200, null=True)),
                ('exp2_company', models.CharField(max_length=200, null=True)),
                ('exp2_number', models.CharField(max_length=20, null=True)),
                ('date_1', models.DateField(blank=True, null=True)),
                ('date_2', models.DateField(blank=True, null=True)),
                ('accepted', models.CharField(default='Pending', max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('User', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL)),
                ('joblisting', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applied_applicant', to='PrecoCareCareers.joblisting')),
            ],
        ),
        migrations.AddField(
            model_name='joblisting',
            name='favourite',
            field=models.ManyToManyField(blank=True, default=None, related_name='user_favourite', to='PrecoCareCareers.employee'),
        ),
    ]
