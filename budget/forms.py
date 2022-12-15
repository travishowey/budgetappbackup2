from django import forms
from .models import Transaction
from django.forms import TextInput, NumberInput, DateInput



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['user_name', 'transaction_name', 'transaction_desc', 'transaction_category',
                  'transaction_date', 'transaction_type', 'transaction_amount']
        labels = {
            'transaction_name': ('Title'),
            'transaction_desc': ('Description'),
            'transaction_type': ('Type (debit or income)'),
            'transaction_date': ('Date'),
            'transaction_category': ('Category'),
            'transaction_amount': ('Amount'),
            'user_name': ('User'),
        }

        widgets = {
            'user_name': forms.Select(attrs={
                'class': 'form-control mb-2',
                # 'style': 'display: none;'
            }),
            'transaction_name': TextInput(attrs={
                'class': 'form-control mb-2',
            }),
            'transaction_desc': TextInput(attrs={
                'class': 'form-control',
            }),
            'transaction_category': forms.Select(attrs={
                'class': 'form-control mb-2',
            }),
            'transaction_type': forms.Select(attrs={
                'class': 'form-control mb-2',
            }),

            'transaction_date': forms.DateInput(format=('%d/%m/%Y'),
                attrs={
                'class': 'form-control mb-2',
            }),
        }
