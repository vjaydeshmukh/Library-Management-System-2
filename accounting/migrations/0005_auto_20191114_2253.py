# Generated by Django 2.2.5 on 2019-11-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20191114_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reference_num',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
