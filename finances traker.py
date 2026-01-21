import math
from datetime import datetime
from tracker import load_data, save_data, clear_data, Transaction, Income, Expense
12
def run_tracker():
    # Requirement: Load existing data at startup
    history = load_data()
    summary = {"total_income": 0, "total_expense": 0}
    
    # Calculate summary from loaded data
    for transaction in history:
        if isinstance(transaction, Income):
            summary["total_income"] += transaction.amount
        else:
            summary["total_expense"] += transaction.amount
    
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
            print("Is this income (1) or expense (2)?")
            trans_type = input("Enter 1 for income, 2 for expense: ")
            if trans_type in ["1", "2"]:
                handle_transaction(int(trans_type), history, summary)
            else:
                print("Invalid choice.")
        elif choice == "2":
            display_summary(history, summary)
        elif choice == "3":
            save_data(history)
            print("Data saved!")
        elif choice == "4":
            confirm = input("Are you sure? This cannot be undone! (y/n): ")
            if confirm.lower() == 'y':
                clear_data()
                history = [] # Reset the current session list
                summary = {"total_income": 0, "total_expense": 0} # Reset summary
                print("All data cleared!")
        elif choice == "5":
            save_data(history) # Auto-save on exit
            active = False
            print("Goodbye!")
        else:
            print("Invalid option. Please try again.")
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