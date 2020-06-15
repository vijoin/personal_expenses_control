from django.shortcuts import render, redirect
from .forms import ExpenseForm, ProductExpenseFormSet
from expenses.models import Expenses, ProductExpense


def index(request):
    return render(request, 'expenses/index.html', context={})


def new(request, expense_id=None):
    if expense_id:
        expense = Expenses.objects.get(pk=expense_id)
        form = ExpenseForm(instance=expense)
        formset = ProductExpenseFormSet(queryset=ProductExpense.objects.filter(expense=expense_id))
    else:
        form = ExpenseForm()
        formset = ProductExpenseFormSet(queryset=ProductExpense.objects.none())

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        formset = ProductExpenseFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            if not expense_id:
                expense = form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.expense = expense
                instance.save()

            return redirect('expenses-edit', expense_id=expense.id)

    return render(request, 'expenses/new.html', {
        'form': form,
        'formset': formset})
