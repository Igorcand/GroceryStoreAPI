# Generated by Django 4.1.5 on 2023-01-20 09:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_sale_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]