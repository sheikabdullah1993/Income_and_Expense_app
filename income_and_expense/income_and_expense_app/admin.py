from django.contrib import admin
from .models import IncomeExpense, UserBalance

admin.site.register(IncomeExpense)


admin.site.register(UserBalance)