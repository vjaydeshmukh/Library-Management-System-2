# Generated by Django 2.2.5 on 2019-10-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_document_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
