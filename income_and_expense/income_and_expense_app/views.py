from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserBalance, IncomeExpense
import time
from django.db import models
from django.contrib import messages


def login(request):
    return render(request, "login.html")  #Redirecting to Login Page

#Login Code
def login_validation(request):
    if request.method=='POST':
        global username
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username, password=password)


        if user is not None:
            auth.login(request, user)
            user_balance = UserBalance.objects.filter(username__username=username).values_list('balance', flat=True)[0]

            return render(request, "homepage.html", {'name':username, 'balance':user_balance})
        else:
            messages.error(request, "Invalid Credentials")

    else:
        messages.error(request, "Error")


def create_entry(request):
    return render(request, "createentry.html", {'name':username}) #Redirecting to Create Entry Page



#Create Income/Expense Entry Code
def create_entry_form(request):
    if request.method=='POST':
        entry_type=request.POST.get("expensetype")
        amount=request.POST.get("amount")
        details=request.POST.get("entrydetails")
        capture_date=time.strftime('%Y-%m-%d')

        IncomeExpense.objects.create(entry_type=entry_type, amount=amount, details=details, capture_date=capture_date, username=request.user)

        user_balance = UserBalance.objects.filter(username=request.user).values_list('balance', flat=True)[0]
        if entry_type=="income":
            total_balance = int(user_balance) + int(amount)
        else:
            total_balance=int(user_balance) - int(amount)

        update_balance=UserBalance.objects.get(username=request.user)
        update_balance.balance=total_balance
        update_balance.save()
        return render(request, "homepage.html", {'name':username, 'balance':total_balance})

    else:
        messages.error(request, "Error")



#Code for viewing Income/Expense record filtered by username
def view_entry(request):
    list_values=IncomeExpense.objects.all().filter(username=request.user)
    return render(request,"view-entry.html",{'name':username,'list_values':list_values})


#Code for Deleting Income/Expense Entry
def delete_income(request, id):
        income = IncomeExpense.objects.get(id=id)
        user_balance = UserBalance.objects.filter(username=request.user).values_list('balance', flat=True)[0]
        income.delete()
        return render(request, "homepage.html", {'name':username, 'balance': user_balance})



#Code for Logout
def log_out(request):
    return render(request, "login.html")