import unittest
from tracker import Income, Expense, Transaction, load_data, clear_data
import os

class TestFinanceTracker(unittest.TestCase):

    def test_income_details(self):
        income = Income(100, "Salary", "2026-01-22")
        self.assertIn("INCOME", income.get_details())
        self.assertIn("Salary", income.get_details())
    
    def test_expense_details(self):
        expense = Expense(50, "Food", "2026-01-22")
        self.assertIn("EXPENSE", expense.get_details())
        self.assertIn("Food", expense.get_details())
    
    def test_transaction_attributes(self):
        t = Transaction(20, "Misc", "2026-01-22")
        self.assertEqual(t.amount, 20)
        self.assertEqual(t.category, "Misc")
        self.assertTrue(t.is_verified)

    def test_load_clear_data(self):
        # Clear before test
        clear_data()
        history = load_data()
        self.assertEqual(history, [])  # Should be empty

if __name__ == "__main__":
    unittest.main()
