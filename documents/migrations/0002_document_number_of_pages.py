# Generated by Django 2.2.5 on 2019-10-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='number_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]