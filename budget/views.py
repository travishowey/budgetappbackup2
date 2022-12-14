from django.shortcuts import render, redirect
from .models import Transaction, Bill, Category
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from django.core.paginator import Paginator
from django.contrib import messages
from calendar import monthrange
import datetime

# Create your views here.

def calculateBalance(request):
    transaction_list = Transaction.objects.all().values().filter(user_name=request.user.id)
    bill_list = Bill.objects.all().values().filter(user_name=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)

    # Calculate Total Amount (before bills)
    amount_before = 0
    bill_total = 0
    for t in transaction_list:
        if t['transaction_type'] == "Debit":
            amount_before -= t['transaction_amount']
        if t['transaction_type'] == "Income":
            amount_before += t['transaction_amount']
    for b in bill_list:
        bill_total += b['bill_amount']
    # Save details to profile (converts type from money to decimal)
    profile.before_balance = amount_before
    profile.available_balance = amount_before - bill_total
    profile.save()

def calculateWidget(request, widgetRequest):
    profile = Profile.objects.get(user_id=request.user.id)

    # Calculate Days in Month
    weekday, totalDays = monthrange(profile.payday.year, profile.payday.month)
    currentDate = datetime.datetime.now()
    currentM = currentDate.strftime("%b")
    currentMonth = currentDate.strftime("%B")

    # Spending Rate
    if widgetRequest == "spendingRate":
        spendingRate = profile.available_balance // totalDays
        return totalDays, currentDate, currentM, spendingRate,
    # Monthly Spending
    if widgetRequest == "monthlySpending":
        transaction_list = Transaction.objects.all().values().filter(user_name=request.user.id).filter(transaction_date__month=currentDate.month )
        # Calculate Total Amount (before bills)
        debit_amount = 0.00
        income_amount = 0.00
        for t in transaction_list:
            if t['transaction_type'] == "Debit":
                debit_amount += float(t['transaction_amount'])
            if t['transaction_type'] == "Income":
                income_amount += float(t['transaction_amount'])
        if profile.available_balance != 0:
            remaining_balance = float(profile.available_balance) - debit_amount
            spendingpercent = (debit_amount / float(profile.available_balance)) * 100
        else:
            remaining_balance = 0
            spendingpercent = 0
        return debit_amount, income_amount, currentMonth, remaining_balance, spendingpercent


@login_required
def index(request):
    transaction_list = Transaction.objects.all().order_by('-transaction_date').values().filter(user_name=request.user.id)[:5]
    bill_list = Bill.objects.all().values().filter(user_name=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)

    calculateBalance(request)
    debit_amount, income_amount, currentMonth, remaining_balance, spendingpercent = calculateWidget(request, "monthlySpending")
    totalDays, currentDate, currentM, spendingRate = calculateWidget(request, "spendingRate")


    context = {
        'transaction_list': transaction_list,
        'bill_list': bill_list,
        'profile': profile,
        'totalDays': totalDays,
        'currentDate': currentDate,
        'currentM': currentM,
        'currentMonth': currentMonth,
        'spendingRate': spendingRate,
        'debit_amount': debit_amount,
        'income_amount': income_amount,
        'remaining_balance': remaining_balance,
        'spendingpercent': spendingpercent
    }
    return render(request, 'budget/dashboard.html', context)

@login_required
def wallet(request):
    transaction_list = Transaction.objects.all().order_by('-transaction_date').values().filter(user_name=request.user.id)
    bill_list = Bill.objects.all().values().filter(user_name=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)

    calculateBalance(request)

    # Pagination
    paginator = Paginator(transaction_list, 5)
    page = request.GET.get('page')
    transaction_list = paginator.get_page(page)

    context = {
        'transaction_list': transaction_list,
        'bill_list': bill_list,
        'profile': profile,
    }
    return render(request, 'budget/wallet.html', context)

@login_required
def spending(request):
    transaction_list = Transaction.objects.all().order_by('-transaction_date').values().filter(user_name=request.user.id)
    bill_list = Bill.objects.all().filter(user_name=request.user.id)
    category_list = Category.objects.all()
    profile = Profile.objects.get(user_id=request.user.id)

    debit_amount, income_amount, currentMonth, remaining_balance, spendingpercent = calculateWidget(request, "monthlySpending")
    totalDays, currentDate, currentM, spendingRate = calculateWidget(request, "spendingRate")


    context = {
        'transaction_list': transaction_list,
        'bill_list': bill_list,
        'category_list': category_list,
        'profile': profile,
        'totalDays': totalDays,
        'currentDate': currentDate,
        'currentM': currentM,
        'currentMonth': currentMonth,
        'spendingRate': spendingRate,
        'debit_amount': debit_amount,
        'income_amount': income_amount,
        'remaining_balance': remaining_balance,
        'spendingpercent': spendingpercent

    }
    return render(request, 'budget/spending.html', context)

@login_required
def reports(request):
    return render(request, 'budget/reports.html')


@login_required
def create_transaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f"Transaction successfully added.")
        calculateBalance(request)
        return redirect('budget:wallet')
    return render(request, 'budget/transaction-form-create.html', {'form': form})

@login_required
def delete_transaction(request, id):
    transaction = Transaction.objects.get(id=id)
    if request.method == "POST":
        transaction.delete()
        messages.success(request, f"Transaction successfully deleted.")
        calculateBalance(request)
        return redirect('budget:wallet')
    return render(request, 'budget/transaction-delete.html', {'transaction': transaction})

@login_required
def edit_transaction(request, id):
    transaction = Transaction.objects.get(id=id)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        messages.success(request, f"Transaction successfully updated.")
        calculateBalance(request)
        return redirect('budget:wallet')
    return render(request, 'budget/transaction-form-update.html', {'transaction': transaction, 'form': form})


