# Generated by Django 2.1.2 on 2018-10-15 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20181015_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='summary',
        ),
        migrations.AddField(
            model_name='job',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]