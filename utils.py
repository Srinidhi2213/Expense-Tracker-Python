# Imports
import matplotlib.pyplot as plt
import datetime
from dataclasses import asdict

# Input validation
def get_valid_amount():
    while True:
        try:
            amount = float(input(">>> Enter Amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_date():
    date_str = input(">>> Enter Date (YYYY-MM-DD) [Leave empty for today]: ")
    if not date_str:
        return datetime.date.today().strftime("%Y-%m-%d")
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Invalid format. Using today's date instead.")
        return datetime.date.today().strftime("%Y-%m-%d")

# Visualization of expenses
def plot_expenses(expenses):
    if len(expenses) == 0:
        print("No data to visualize.")
        return

    data = {}
    for exp in expenses:
        data[exp.category] = data.get(exp.category, 0) + exp.amount

    categories = list(data.keys())
    amounts = list(data.values())

    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Spending by Category')
    plt.show()
