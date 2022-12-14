from django import forms
from .models import Transaction
from django.forms import TextInput, NumberInput, DateInput
from django.utils.translation import ugettext_lazy as _



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['user_name', 'transaction_name', 'transaction_desc', 'transaction_category',
                  'transaction_date', 'transaction_type', 'transaction_amount']
        labels = {
            'transaction_name': _('Title'),
            'transaction_desc': _('Description'),
            'transaction_type': _('Type (debit or income)'),
            'transaction_date': _('Date'),
            'transaction_category': _('Category'),
            'transaction_amount': _('Amount'),
            'user_name': _('User'),
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