# Generated by Django 2.1.11 on 2019-10-03 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20190921_0220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='rsvps',
        ),
    ]
