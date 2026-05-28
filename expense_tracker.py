# Imports
import json
import os
from dataclasses import dataclass, asdict
from utils import *

"""EXPENSE DATA STRUCTURE"""
@dataclass
class Expense:
    id: int
    amount: float
    category: str
    date: str
    description: str

"""EXPENSE MANGAER CLASS"""
class ExpenseManager:

    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_data()

    def load_data(self):
        """Loads data from the JSON file into a list of Expense objects"""
        # Check if the JSON file exists
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            data = json.load(f)
        # Convert the list of dicts back into Expense objects
        return [Expense(**record) for record in data]

    def save_data(self):
        """Saves the current list of expenses to the JSON file"""
        with open(self.filename, 'w') as file:
            # Convert Expense objects to dicts for JSON serialization
            data = [asdict(exp) for exp in self.expenses]
            json.dump(data, file, indent=4)

    def add_expense(self, amount, category, date, description):
        """Adds a new expense and saves immediately"""
        # Generate a simple ID (max ID + 1)
        new_id = 1
        if self.expenses:
            new_id = max(exp.id for exp in self.expenses) + 1
        
        new_expense = Expense(new_id, amount, category, date, description)
        self.expenses.append(new_expense)
        self.save_data()
        print("Expense added successfully.")

    def get_all_expenses(self):
        return self.expenses

    def get_total_spending(self):
        """Calculates total spending using Python's sum()"""
        return sum(exp.amount for exp in self.expenses)

    def delete_expense(self, expense_id):
        """Deletes an expense by ID"""
        # Filter out the expense with the matching ID
        initial_count = len(self.expenses)
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
        
        if len(self.expenses) < initial_count:
            self.save_data()
            print("Expense deleted.")
        else:
            print("No expense found with that ID.")
