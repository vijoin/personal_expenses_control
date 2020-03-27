from django.contrib import admin
from .models import Expenses, ProductExpense

class ProductExpenseInline(admin.TabularInline):
    model = ProductExpense

class ExpenseAdmin(admin.ModelAdmin):
    inlines = [
        ProductExpenseInline,
    ]


admin.site.register(Expenses, ExpenseAdmin)
admin.site.register(ProductExpense)
