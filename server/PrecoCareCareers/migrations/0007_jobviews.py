# Generated by Django 4.1 on 2022-08-27 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PrecoCareCareers', '0006_joblisting_date_created_employee_applicantmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views_count', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('joblisting', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_count', to='PrecoCareCareers.joblisting')),
            ],
        ),
    ]
