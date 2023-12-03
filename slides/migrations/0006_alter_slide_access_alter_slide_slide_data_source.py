# Generated by Django 4.1.3 on 2023-12-01 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0021_alter_block_component'),
        ('slides', '0005_remove_slide_privacy_slide_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=100),
        ),
        migrations.AlterField(
            model_name='slide',
            name='slide_data_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slide_data_source_sheet', to='sheets.sheet'),
        ),
    ]
