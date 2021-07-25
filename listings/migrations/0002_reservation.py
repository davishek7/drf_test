# Generated by Django 3.2 on 2021-07-23 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('booking_info', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_info', to='listings.bookinginfo')),
            ],
        ),
    ]
