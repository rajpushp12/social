# Generated by Django 3.2.5 on 2021-08-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_connections_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=32),
        ),
    ]
