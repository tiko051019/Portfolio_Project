# Generated by Django 5.1.6 on 2025-05-05 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_rename_ip_visitordata_ipv6'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VisitorJustEnterIP',
        ),
    ]
