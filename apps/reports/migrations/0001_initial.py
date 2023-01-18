# Generated by Django 4.1.5 on 2023-01-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('quantity_itens', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('sale', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
