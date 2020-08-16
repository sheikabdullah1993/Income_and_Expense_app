from django.db import models
from django.contrib.auth.models import User

class IncomeExpense(models.Model):
    entry_type=models.CharField(max_length=100)
    amount=models.IntegerField()
    details=models.TextField()
    capture_date=models.DateField()
    username=models.ForeignKey(User, on_delete=models.CASCADE)


class UserBalance(models.Model):
    balance=models.IntegerField()
    username=models.ForeignKey(User, on_delete=models.CASCADE)
