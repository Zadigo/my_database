# Generated by Django 4.1.3 on 2023-12-01 17:54

from django.db import migrations, models
import my_database.validators


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='privacy',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=100),
        ),
        migrations.AlterField(
            model_name='slide',
            name='slide_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, validators=[my_database.validators.validate_id]),
        ),
    ]
