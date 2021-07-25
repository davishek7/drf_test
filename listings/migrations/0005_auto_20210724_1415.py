# Generated by Django 3.2 on 2021-07-24 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20210724_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='listing',
        ),
        migrations.AddField(
            model_name='reservation',
            name='booking_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_info', to='listings.bookinginfo'),
        ),
    ]