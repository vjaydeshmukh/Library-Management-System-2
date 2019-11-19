# Generated by Django 2.2.5 on 2019-11-19 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0013_auto_20191118_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'Pending'), (20, 'Pending Overdue'), (30, 'Done'), (40, 'Done Overdue')], default=10),
            preserve_default=False,
        ),
    ]
