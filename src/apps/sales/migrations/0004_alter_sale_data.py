# Generated by Django 4.1.5 on 2023-01-20 09:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sale_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
