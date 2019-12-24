# Generated by Django 2.2.1 on 2019-12-24 03:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('attachment', models.FileField(upload_to='')),
                ('send_it', models.BooleanField(default=False)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Emails to send',
                'verbose_name_plural': 'Emails to send',
            },
        ),
    ]
