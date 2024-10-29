# Expense.py
import sys
from PyQt5.QtWidgets import QApplication
from app.expense_controller import ExpenseApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("app/ui/style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())