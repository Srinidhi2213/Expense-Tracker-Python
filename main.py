# Imports
from utils import *
from expense_tracker import ExpenseManager

# Main function
def main(budget_limit=1000.0):
    manager = ExpenseManager()

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Visualize Spending")
        print("4. Check Budget Status")
        print("5. Delete Expense")
        print("6. Exit\n")

        choice = input(">>> Choose an option: ")

        if choice == '1':
            amt = get_valid_amount()
            cat = input(">>> Enter Category (Food, Rent, etc...): ").capitalize()
            date = get_valid_date()
            desc = input(">>> Enter Description: ")
            manager.add_expense(amt, cat, date, desc)

        elif choice == '2':
            expenses = manager.get_all_expenses()
            header = "\nID | Date       | Category    | Amount      | Description"
            print(header)
            print("-" * (len(header) + 10))
            for exp in expenses:
                print(f"{exp.id:<3}| {exp.date} | {exp.category:<11} | ${exp.amount:<10} | {exp.description}")

        elif choice == '3':
            plot_expenses(manager.get_all_expenses())

        elif choice == '4':
            total = manager.get_total_spending()
            print(f"\nTotal: ${total:.2f} / Budget: ${budget_limit:.2f}")
            if total > budget_limit:
                print(f"OVER BUDGET by ${total - budget_limit:.2f}")

        elif choice == '5':
            try:
                e_id = int(input(">>> ID to delete: "))
                manager.delete_expense(e_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == '6':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
