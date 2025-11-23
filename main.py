from datetime import datetime
from colorama import Fore, Style
import os

from services  import ExpenseRepository

expenseRepository = ExpenseRepository()

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "╔════════════════════════╗")
        print("║     EXPENSE TRACKER    ║")
        print("╚════════════════════════╝" + Style.RESET_ALL)
        print(Fore.YELLOW +"1) Add expense" + Style.RESET_ALL)
        print(Fore.YELLOW +"2) List all expenses" + Style.RESET_ALL)
        print(Fore.YELLOW +"3) Search by category" + Style.RESET_ALL)
        print(Fore.YELLOW +"4) Search by amount range" + Style.RESET_ALL)
        print(Fore.YELLOW +"5) Search by date" + Style.RESET_ALL)
        print(Fore.YELLOW +"6) Total of all expenses" + Style.RESET_ALL)
        print(Fore.YELLOW +"7) Total by category" + Style.RESET_ALL)
        print(Fore.YELLOW +"8) Most expensive expense" + Style.RESET_ALL)
        print(Fore.RED +"9) Exit" + Style.RESET_ALL)

        choice = input("Enter choice: ")

        match choice:
            case "1":
                expenseRepository.add_expense()

            case "2":
                expenseRepository.print_expenses()

            case "3":
                cat = input("Enter category: ")
                results = expenseRepository.search_by_category(cat)
                for r in results:
                    print(f"Description: {r.description} | Amount: ${r.amount:.2f} | Category: {r.category} | Date: {r.date}")

            case "4":
                mn = float(input("Min amount: "))
                mx = float(input("Max amount: "))
                results = expenseRepository.search_by_amount_range(mn, mx)
                for r in results:
                    print(f"Description: {r.description} | Amount: ${r.amount:.2f} | Category: {r.category} | Date: {r.date}")

            case "5":
                while True:
                    try:
                      date_input = input("Enter date (YYYY-MM-DD): ")
                      target_date = datetime.strptime(date_input, "%Y-%m-%d").date()
                      break
                    except ValueError:
                        print("Invalid date. Try again")
                results = expenseRepository.search_by_date(target_date)
                for r in results:
                    print(f"Description: {r.description} | Amount: ${r.amount:.2f} | Category: {r.category} | Date: {r.date}")

            case "6":
                print("Total:", expenseRepository.total_expenses())

            case "7":
                cat = input("Enter category: ")
                print("Total:", expenseRepository.total_expenses_category(cat))

            case "8":
                result = expenseRepository.most_expenses()
                if isinstance(result, str):
                   print("Most expensive:", result)
                else:
                    description, amount, category, date = result
                    print(f"Most expensive: {description} (Category: {category}, Amount: ${amount:.2f}, Date: {date})")

            case "9":
                expenseRepository.save_data()
                print("Goodbye!")
                break

            case _:
                print("Invalid choice")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()
