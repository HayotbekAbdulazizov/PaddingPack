# Generated by Django 4.0.2 on 2022-02-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_aboutitem_aboutitemtranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutitemtranslation',
            name='title',
            field=models.CharField(blank=True, max_length=300, verbose_name='Title'),
        ),
    ]
