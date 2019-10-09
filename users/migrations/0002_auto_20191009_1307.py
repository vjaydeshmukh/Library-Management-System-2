# Generated by Django 2.2.5 on 2019-10-09 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('total_issues', models.PositiveIntegerField(blank=True, null=True)),
                ('total_concurrent_issues', models.PositiveIntegerField(blank=True, null=True)),
                ('total_reserves', models.PositiveIntegerField(blank=True, null=True)),
                ('total_renews', models.PositiveIntegerField(blank=True, null=True)),
                ('issue_duration', models.DurationField(blank=True, null=True)),
                ('renew_duration', models.DurationField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('fine_amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='max_checkout',
        ),
        migrations.AddField(
            model_name='member',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Membership'),
        ),
    ]