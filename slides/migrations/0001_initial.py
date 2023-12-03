# Generated by Django 4.1.3 on 2023-12-01 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sheets.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sheets', '0016_alter_block_component_alter_page_privacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slide_id', models.CharField(blank=True, max_length=100, null=True, unique=True, validators=[sheets.validators.validate_id])),
                ('slide_data_source', models.CharField(blank=True, help_text='Top level slide data source', max_length=100, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('privacy', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=100)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('blocks', models.ManyToManyField(blank=True, to='sheets.block')),
                ('sheets', models.ManyToManyField(blank=True, to='sheets.sheet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
