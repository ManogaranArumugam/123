# Generated by Django 2.0.5 on 2018-09-26 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0006_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='level',
        ),
        migrations.RemoveField(
            model_name='department',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='department',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='department',
            name='tree_id',
        ),
    ]