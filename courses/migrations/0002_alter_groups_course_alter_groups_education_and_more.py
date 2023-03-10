# Generated by Django 4.1.4 on 2023-01-12 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='education',
            field=models.CharField(blank=True, choices=[('online', 'Online'), ('offline', 'Offline')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='groups',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('waiting', 'Waiting')], max_length=10, null=True),
        ),
    ]
