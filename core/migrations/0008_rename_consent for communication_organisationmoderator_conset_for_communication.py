# Generated by Django 3.2.7 on 2022-06-23 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220623_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisationmoderator',
            old_name='Consent for communication',
            new_name='conset_for_communication',
        ),
    ]
