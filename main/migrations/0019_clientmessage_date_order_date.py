# Generated by Django 4.0.2 on 2022-02-11 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_clientmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmessage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
