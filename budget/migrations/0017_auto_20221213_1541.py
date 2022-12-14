# Generated by Django 2.2 on 2022-12-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0016_bill_bill_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='budget_balance',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='budget_income',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
