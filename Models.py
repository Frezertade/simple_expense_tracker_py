from datetime import datetime

class Expense:
    def __init__(self, category, description, date, amount):
        self.category = category
        self.description = description
        self.date = date
        self.amount = amount

