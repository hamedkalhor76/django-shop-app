# Generated by Django 4.1.1 on 2022-10-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='authority',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
