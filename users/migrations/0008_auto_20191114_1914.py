# Generated by Django 2.2.5 on 2019-11-14 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_group_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='sender_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='severity',
            field=models.IntegerField(choices=[(10, 'Info'), (20, 'Warning'), (30, 'Alert'), (40, 'Critical')], default=10),
        ),
        migrations.AddField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]