# Generated by Django 5.0.3 on 2024-05-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(null=True)),
                ('DrivingLicene', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('Bookingdate', models.DateTimeField(null=True)),
                ('Returndate', models.DateTimeField(null=True)),
                ('City', models.CharField(max_length=35)),
                ('State', models.CharField(max_length=50)),
                ('Pincode', models.IntegerField(max_length=25)),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
    ]
