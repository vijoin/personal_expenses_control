from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ExpenseForm, ProductExpenseFormSet
from expenses.models import Expenses, ProductExpense


@login_required
def index(request):
    user = request.user
    expenses = Expenses.objects.filter(user=user).all()
    return render(request, 'expenses/index.html', {'expenses': expenses})


@login_required
def new(request, expense_id=None):
    if expense_id:
        expense = Expenses.objects.get(pk=expense_id)
        form = ExpenseForm(instance=expense)
        formset = ProductExpenseFormSet(queryset=ProductExpense.objects.filter(expense=expense_id))
    else:
        form = ExpenseForm()
        formset = ProductExpenseFormSet(queryset=ProductExpense.objects.none())

    if request.method == 'POST':
        if expense_id:
            form = ExpenseForm(request.POST, instance=expense)
        else:
            form = ExpenseForm(request.POST)
        formset = ProductExpenseFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.expense = expense
                instance.save()

            return redirect('expenses-edit', expense_id=expense.id)

    return render(request, 'expenses/new.html', {
        'form': form,
        'formset': formset})
