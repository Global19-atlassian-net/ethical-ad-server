# Generated by Django 2.2.13 on 2020-10-30 16:34
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0037_add_pixel_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='advertisement',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offers', to='adserver.Advertisement'),
        ),
    ]
