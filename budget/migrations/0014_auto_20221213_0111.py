# Generated by Django 2.2 on 2022-12-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0013_bill_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bill_amount_currency',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='budget_balance_currency',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='budget_income_currency',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_amount_currency',
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_amount',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget_balance',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget_income',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_amount',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
