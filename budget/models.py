from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)

class Transaction(models.Model):
    def __str__(self):
        return self.transaction_name

    type_choices = (
        ('Income', 'Income'),
        ('Debit', 'Debit')
    )
    categories = (
        ('General', 'General'),
        ('Auto & Transport', 'Auto & Transport'),
        ('Bills & Utilities', 'Bills & Utilities'),
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Fees & Charges', 'Fees & Charges'),
        ('Financial', 'Financial'),
        ('Food & Dining', 'Food & Dining'),
        ('Gifts & Donations', 'Gifts & Donations'),
        ('Groceries', 'Groceries'),
        ('Health & Fitness', 'Health & Fitness'),
        ('Income', 'Income'),
        ('Investments', 'Investments'),
        ('Kids', 'Kids'),
        ('Pets', 'Pets'),
        ('Shopping', 'Shopping'),
        ('Taxes', 'Taxes'),
        ('Transfer', 'Transfer'),
        ('Travel', 'Travel'),
        ('Other', 'Other'),
    )

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    transaction_name = models.CharField(max_length=200, default="")
    transaction_desc = models.CharField(max_length=500, default="")
    transaction_category = models.CharField(max_length=200, choices=categories, default="Generic")
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=15, choices=type_choices, default="Debit")
    transaction_amount = models.DecimalField(max_digits=11, decimal_places=2, default=0)

class Bill(models.Model):
    def __str__(self):
        return self.bill_name

    bill_name = models.CharField(max_length=200)
    bill_dueDate = models.DateField()
    bill_amount = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


