# Generated by Django 4.1.3 on 2023-11-04 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheet',
            old_name='file',
            new_name='csv_file',
        ),
    ]