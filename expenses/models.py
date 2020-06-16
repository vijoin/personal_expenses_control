from django.db import models


class Expenses(models.Model):
    name = models.CharField(max_length=100)
    # Todo user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()  # ToDo Use NOW  as default

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.id} - {self.name}"

    @property
    def total(self):
        return sum(self.productexpense_set.values_list('amount', flat=True))

class ProductExpense(models.Model):
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    qty = models.FloatField()
    amount = models.FloatField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.expense} - {self.qty} | {self.amount}"
