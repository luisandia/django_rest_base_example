# Generated by Django 3.0.2 on 2020-01-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20200108_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='udpated',
        ),
        migrations.AddField(
            model_name='status',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
