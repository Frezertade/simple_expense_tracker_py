from flask import Flask, render_template
from services import ExpenseRepository


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TESTING"] = True
app.config["PORT"] = 5000
exp_repository = ExpenseRepository()
@app.route('/home')
def home():
    return  render_template("totalExpense.html", data=exp_repository.total_expenses())

@app.route('/expenses')
def list_expenses():
    return render_template("list_expenses.html", data=exp_repository.expenses())


@app.route('/')
def index():
   return "Welcome to Expense Tracker App"

if __name__ == '__main__':
    app.run(debug=True)