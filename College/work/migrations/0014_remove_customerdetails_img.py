# Generated by Django 5.0.3 on 2024-05-12 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0013_rename_carname_orders_carid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='img',
        ),
    ]