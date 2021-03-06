# Generated by Django 4.0.4 on 2022-05-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactForm', '0004_remove_contactformentry_site_admin_notified_by_email_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='contactformentry',
            constraint=models.CheckConstraint(check=models.Q(('name__length__gt', 0)), name='CHECK__ContactFormEntry__name__length_GT_0'),
        ),
    ]
