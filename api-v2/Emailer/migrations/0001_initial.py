# Generated by Django 4.0.4 on 2022-06-02 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('blind_carbon_copies', models.ManyToManyField(blank=True, related_name='bcc_of', to='Emailer.emailuser')),
                ('carbon_copies', models.ManyToManyField(blank=True, related_name='cc_of', to='Emailer.emailuser')),
                ('recipients', models.ManyToManyField(related_name='recipient_of', to='Emailer.emailuser')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_of', to='Emailer.emailuser')),
            ],
        ),
    ]
