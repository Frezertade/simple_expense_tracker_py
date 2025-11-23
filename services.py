import datetime
import os
from Models import Expense
import json


class ExpenseRepository():
    EXPENSE_FILE_NAME = "expenses.json"
    def __init__(self):
        self.expenses = self.load_data()

    def add_expense(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            category = input('Enter category:')
            while True:
                try:
                    amount = float(input('Enter amount:'))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number (e.g., 50.00).")

            description = input('Enter description:')
            self.expenses.append(Expense(category, description, datetime.date.today(), amount))
            print(f"Expense: {description} Amount: ${amount} is Added!")
            another_expense = input('Do you want to enter another expense: Y/N')
            if another_expense.upper() != 'Y':
                break

    def save_data(self):
        with open(self.EXPENSE_FILE_NAME, "w") as file:
            expenseList = []
            for expense in self.expenses:
                expenseList.append(expense.to_dict())
            json.dump(expenseList, file, indent=4)

    def load_data(self):
        try:
         with open(self.EXPENSE_FILE_NAME, "r") as file:
            expenseList = json.load(file)
            loaded_expenses = []
            for expense in expenseList:
                loaded_expenses.append(
                    Expense(expense["category"],
                            expense["description"],
                            datetime.datetime.strptime(expense["date"], "%Y-%m-%d").date(),
                            expense["amount"]))
            return loaded_expenses
        except FileNotFoundError as e:
            print(e)
            return []


    def print_expenses(self):
        for r in self.expenses:
         print(f"Description: {r.description} | Amount: ${r.amount:.2f} | Category: {r.category} | Date: {r.date}")
    def search_by_category(self, category):
      category_expenses = []
      for expense in self.expenses:
        if expense.category == category:
           category_expenses.append(expense)
      return category_expenses

    def search_by_amount_range(self, min, max):
      amount_range_expenses = []
      for expense in self.expenses:
        if min <= expense.amount <= max:
           amount_range_expenses.append(expense)
      return amount_range_expenses


    def search_by_date(self, date):
      date_expenses = []
      for expense in self.expenses:
        if date == expense.date:
           date_expenses.append(expense)
      return date_expenses

    def total_expenses(self):
      total = 0
      for expense in self.expenses:
         total += expense.amount
      return total

    def total_expenses_category(self, category):
        expenses = self.search_by_category(category)
        maxCatExpense = 0
        for exp in expenses:
            maxCatExpense += exp.amount
        return maxCatExpense

    def most_expenses(self):
      if not self.expenses:
        return "No expenses recorded yet."  # Added safe return for empty list

      max = 0
      maxExpense = None
      for expense in self.expenses:
        if expense.amount > max:
            max = expense.amount
            maxExpense = expense
      return maxExpense.description, maxExpense.amount, maxExpense.category, maxExpense.date
