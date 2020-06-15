from django.db import models


class Expenses(models.Model):
    name = models.CharField(max_length=100)
    # Todo user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()  # ToDo Use NOW  as default
    products_expense = models.ManyToOneRel('expense_id', 'ProductExpense', 'expense_id')
    #ToDo Products Purchased/Expensed (o2m)

    def __str__(self):
        return f"{self.id} - {self.name}"


class ProductExpense(models.Model):
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.FloatField()
    price = models.FloatField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.expense_id} - {self.amount} | {self.price}"
