# Generated by Django 2.0.5 on 2018-05-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='productos'),
        ),
    ]