# Generated by Django 4.1.3 on 2023-12-01 21:36

from django.db import migrations, models
import my_database.validators


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0007_alter_slide_access_alter_slide_slide_data_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('block_id', models.CharField(blank=True, max_length=100, null=True, unique=True, validators=[my_database.validators.validate_id])),
                ('component', models.CharField(choices=[('table-block', 'Table Block'), ('graph-block', 'Graph Block'), ('grid-block', 'Grid Block'), ('chart-block', 'Chart Block')], default='table-block', max_length=100)),
                ('record_creation_fields', models.JSONField(blank=True, help_text='Fields to consider when creating a new record', null=True)),
                ('record_update_fields', models.JSONField(blank=True, help_text='Fields to consider when updating a new record', null=True)),
                ('block_url_source', models.URLField(blank=True, help_text='Block level data source', null=True)),
                ('search_columns', models.JSONField(blank=True, help_text='The columns to use for searching data', null=True)),
                ('user_filters', models.JSONField(blank=True, help_text='The filters the user is allowed to use', null=True)),
                ('conditions', models.JSONField(blank=True, help_text='Internal block configuration', null=True)),
                ('active', models.BooleanField(default=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.AlterField(
            model_name='slide',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=100),
        ),
        migrations.AlterField(
            model_name='slide',
            name='blocks',
            field=models.ManyToManyField(blank=True, to='slides.block'),
        ),
    ]
