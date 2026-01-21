import math
from datetime import datetime

# Requirement: OOP - Parent Class
class Transaction:
    def __init__(self, amount: float, category: str, date: str):
        # Requirement: Primitives (float, str)
        self.amount = amount
        self.category = category
        self.date = date
        self.is_verified = True # Requirement: Primitive (bool)

    def get_details(self):
        return f"[{self.date}] {self.category}: ${self.amount:.2f}"

# Requirement: OOP - Child Class 1 (Inheritance)
class Income(Transaction):
    # Requirement: Polymorphism (Overriding method)
    def get_details(self):
        return f"[INCOME] {super().get_details()}"

# Requirement: OOP - Child Class 2 (Inheritance)
class Expense(Transaction):
    def get_details(self):
        return f"[EXPENSE] {super().get_details()}"

def run_tracker():
    # Requirement: Load existing data at startup
    history = load_data()
    
    active = True
    while active:
        print("\n--- Finance Tracker Menu ---")
        print("1. Add Transaction")
        print("2. View History")
        print("3. Save Data")
        print("4. Delete All Data (Fresh Start)")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            # (Logic to add income/expense)
            pass 
        elif choice == "2":
            # (Logic to print history)
            pass
        elif choice == "3":
            save_data(history)
        elif choice == "4":
            confirm = input("Are you sure? This cannot be undone! (y/n): ")
            if confirm.lower() == 'y':
                clear_data()
                history = [] # Reset the current session list
        elif choice == "5":
            save_data(history) # Auto-save on exit
            active = False
def handle_transaction(choice, history, summary):
    try:
        amt = float(input("Enter amount: "))
        cat = input("Enter category (e.g., Salary, Food): ")
        date = datetime.now().strftime("%Y-%m-%d")

        if choice == 1:
            t = Income(amt, cat, date)
            summary["total_income"] += amt
        else:
            t = Expense(amt, cat, date)
            summary["total_expense"] += amt
        
        history.append(t)
        print("Transaction saved!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_summary(history, summary):
    print("\n--- History ---")
    # Requirement: Control Structure (For loop & If/Else)
    if not history:
        print("No transactions yet.")
    else:
        for item in history:
            print(item.get_details())
    
    balance = summary["total_income"] - summary["total_expense"]
    print(f"\nNet Balance: ${balance:.2f}")

if __name__ == "__main__":
    run_tracker()