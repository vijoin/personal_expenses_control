from django import forms
from django.forms import modelformset_factory

from .models import Expenses, ProductExpense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'location', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }


class ProductExpenseForm(forms.ModelForm):
    class Meta:
        model = ProductExpense
        fields = ['product', 'qty', 'amount', 'comment']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
        }


ProductExpenseFormSet = modelformset_factory(
    ProductExpense,
    form=ProductExpenseForm,
    fields=('product', 'qty', 'amount', 'comment')
)
