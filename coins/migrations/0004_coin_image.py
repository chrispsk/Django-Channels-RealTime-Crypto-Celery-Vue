# Generated by Django 3.2 on 2021-04-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0003_alter_coin_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
