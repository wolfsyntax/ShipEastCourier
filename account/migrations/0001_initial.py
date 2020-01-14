# Generated by Django 2.2.1 on 2019-12-28 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackcode', models.SlugField(max_length=32)),
                ('courier', models.CharField(max_length=255)),
                ('merchant', models.CharField(max_length=255)),
                ('item_name', models.CharField(max_length=255)),
                ('parcel_status', models.CharField(choices=[('', 'Parcel Status'), ('pickup', 'Pickup'), ('on process', 'On Process'), ('on delivery', 'On Delivery'), ('delivered', 'Delivered')], max_length=255)),
                ('parcel_price', models.FloatField()),
                ('shipping_fee', models.FloatField()),
                ('date_shipped', models.DateTimeField()),
                ('date_arrived', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tracking Detail',
                'verbose_name_plural': 'Tracking Details',
                'db_table': 'TrackingDetails',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('trn', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=254)),
                ('district', models.CharField(max_length=254)),
                ('parish', models.CharField(choices=[('', 'Choose...'), ('St. Andrew', 'Kingston'), ('Portland', 'St. Thomas'), ('St. Catherine', 'St. Mary'), ('St. Ann', 'Manchester'), ('Clarendon', 'Hanover'), ('Westmoreland', 'St. James'), ('Trelawny', 'St. Elizabeth')], max_length=15)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'Users Profile',
                'db_table': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='MailClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('send_it', models.BooleanField(default=False)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email to send',
                'verbose_name_plural': 'Emails to send',
                'db_table': 'MailClient',
            },
        ),
    ]
