# Generated by Django 4.0.4 on 2022-05-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactForm', '0006_contactformentry_check__contactformentry__email__length_gt_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformentry',
            name='organization',
            field=models.CharField(blank=True, max_length=180),
        ),
    ]
