# Generated by Django 5.1.4 on 2024-12-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_item_options_alter_item_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]