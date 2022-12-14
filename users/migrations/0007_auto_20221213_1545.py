# Generated by Django 2.2 on 2022-12-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20221213_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='available_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
        migrations.AddField(
            model_name='profile',
            name='before_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
