# Generated by Django 4.1.3 on 2023-11-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0008_alter_connnection_token_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connnection',
            name='token_type',
            field=models.CharField(choices=[('Bearer', 'Bearer')], default='Bearer', max_length=50),
        ),
    ]
