# Generated by Django 4.1.3 on 2023-11-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_webhook_webhook_unique_webhook_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='last_usage',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
