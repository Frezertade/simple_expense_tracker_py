import datetime
import os
from Models import Expense

expenses = []

def add_expense():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        category = input('Enter category:')
        amount = float(input('Enter amount:'))
        description = input('Enter description:')
        expenses.append(Expense(category, description, datetime.date.today(), amount))
        print(f"Expense: {description} Amount: ${amount} is Added!")

        another_expense = input('Do you want to enter another expense: Y/N')
        if another_expense.upper() != 'Y':
            break

def print_expenses():
    for r in expenses:
        print(f"Description: {r.description} | Amount: ${r.amount:.2f} | Category: {r.category} | Date: {r.date}")
def search_by_category(category):
    category_expenses = []
    for expense in expenses:
        if expense.category == category:
           category_expenses.append(expense)
    return category_expenses

def search_by_amount_range(min,max):
    amount_range_expenses = []
    for expense in expenses:
        if min <= expense.amount <= max:
           amount_range_expenses.append(expense)
    return amount_range_expenses


def search_by_date(date):
    date_expenses = []
    for expense in expenses:
        if date == expense.date:
           date_expenses.append(expense)
    return date_expenses

def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense.amount
    return total

def total_expenses_category(category):
    expenses = search_by_category(category)
    return total_expenses(expenses)

def most_expenses(expenses):
    if not expenses:
        return "No expenses recorded yet."  # Added safe return for empty list

    max = 0
    maxExpense = None
    for expense in expenses:
        if expense.amount > max:
            max = expense.amount
            maxExpense = expense
    return maxExpense.description, maxExpense.amount, maxExpense.category, maxExpense.date
