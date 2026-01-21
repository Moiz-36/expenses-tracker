
import json
import os

FILE_NAME = "finance_data.json"

class Transaction:
    def __init__(self, amount: float, category: str, date: str):
        self.amount = amount
        self.category = category
        self.date = date
        self.is_verified = True 

    def get_details(self):
        return f"[{self.date}] {self.category}: ${self.amount:.2f}"


class Income(Transaction):
    def get_details(self):
        return f"[INCOME] {super().get_details()}"

class Expense(Transaction):
    def get_details(self):
        return f"[EXPENSE] {super().get_details()}"

def load_data():
    history = []
    if not os.path.exists(FILE_NAME):
        return history

    try:
        with open(FILE_NAME, "r") as f:
            raw_data = json.load(f)
            for item in raw_data:
                if item["type"] == "Income":
                    history.append(Income(item["amount"], item["category"], item["date"]))
                else:
                    history.append(Expense(item["amount"], item["category"], item["date"]))
    except (json.JSONDecodeError, KeyError):
        print("Error reading data file. Starting with empty history.")
    
    return history

def clear_data():
    """Deletes the saved data file."""
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("All previous data has been deleted.")
    else:
        print("No data file found to delete.")
