# Generated by Django 4.1.3 on 2023-09-27 23:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connnection',
            name='access_token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='connnection',
            name='expires_in',
            field=models.PositiveIntegerField(default=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connnection',
            name='scope',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='connnection',
            name='token_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='connnection',
            name='token_type',
            field=models.CharField(
                choices=[('Bearer', 'Bearer')], default='Bearer', max_length=50),
        ),
        migrations.AlterField(
            model_name='connnection',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
