# Generated by Django 5.1.6 on 2025-05-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_visitorip_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorip',
            name='browser',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='visitorip',
            name='device',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='visitorip',
            name='os',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='visitorip',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='visitorip',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
