# Generated by Django 2.2.8 on 2020-06-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring', '0005_auto_20200604_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotpreference',
            name='slot',
        ),
        migrations.AddField(
            model_name='slotpreference',
            name='day',
            field=models.IntegerField(choices=[(1, 'Mon'), (2, 'Tue'), (3, 'Wed'), (4, 'Thu'), (5, 'Fri')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slotpreference',
            name='hour',
            field=models.IntegerField(choices=[(11, '11am'), (12, '12pm'), (13, '1pm'), (14, '2pm'), (15, '3pm'), (16, '4pm')], default=0),
            preserve_default=False,
        ),
    ]