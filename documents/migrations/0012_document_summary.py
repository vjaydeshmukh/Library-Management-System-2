# Generated by Django 2.2.5 on 2019-11-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0011_auto_20191030_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='summary',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
