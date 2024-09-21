# Generated by Django 3.2.25 on 2024-08-15 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20240815_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='check_in_date',
            new_name='checkin_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='check_out_date',
            new_name='checkout_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guest_name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.bookinguser'),
        ),
    ]
