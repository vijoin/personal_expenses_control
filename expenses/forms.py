from django import forms
from .models import Expenses
from products.models import Product


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'Location', 'date']

class ProductExpenseForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    amount = forms.FloatField()
    price = forms.FloatField()
    comment = forms.CharField(widget=forms.Textarea)
