# Generated by Django 2.1.2 on 2018-10-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20181015_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
