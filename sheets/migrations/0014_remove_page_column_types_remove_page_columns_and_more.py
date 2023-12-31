# Generated by Django 4.1.3 on 2023-12-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0013_page_column_types_page_columns_alter_block_component_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='column_types',
        ),
        migrations.RemoveField(
            model_name='page',
            name='columns',
        ),
        migrations.AddField(
            model_name='sheet',
            name='column_types',
            field=models.JSONField(blank=True, help_text='The data type for each column', null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='columns',
            field=models.JSONField(blank=True, help_text='Available columns in the data source', null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='component',
            field=models.CharField(choices=[('table-block', 'Table Block'), ('graph-block', 'Graph Block'), ('grid-block', 'Grid Block'), ('chart-block', 'Chart Block')], default='table-block', max_length=100),
        ),
        migrations.AlterField(
            model_name='page',
            name='privacy',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=100),
        ),
    ]
