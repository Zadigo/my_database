# Generated by Django 4.1.3 on 2023-11-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_rename_token_id_connnection_id_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connnection',
            name='token_type',
            field=models.CharField(choices=[('Bearer', 'Bearer')], default='Bearer', max_length=50),
        ),
    ]
