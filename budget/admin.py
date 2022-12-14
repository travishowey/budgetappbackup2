from django.contrib import admin
from .models import Transaction, Bill, Category


# Register your models here.
admin.site.register(Transaction)
admin.site.register(Bill)
admin.site.register(Category)
