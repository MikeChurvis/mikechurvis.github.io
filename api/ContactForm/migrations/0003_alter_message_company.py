# Generated by Django 3.2.4 on 2021-11-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactForm', '0002_message_contactform_sent_at_a9fe2d_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
