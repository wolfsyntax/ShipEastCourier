# Generated by Django 2.2.1 on 2019-12-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_mailclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailclient',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]