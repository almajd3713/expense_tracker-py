# expense_controller.py
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from app.ui.expense_ui import ExpenseUI

class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 400)
        self.center()
        # Create the UI and set it as the central widget
        self.ui = ExpenseUI()
        self.setCentralWidget(self.ui)

        # Connect the button to the add_expense method
        self.ui.input_panel.add_button.clicked.connect(self.add_expense)

        # Connect the row_deleted signal to the delete_expense method
        self.ui.expense_table.row_deleted.connect(self.delete_expense)

        # Add default data
        self.add_default_data()

    def center(self):
        """Center the window on the screen."""
        frame = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def add_default_data(self):
        initial_data = [("Groceries", 50.0), ("Fuel", 70.0), ("Gym", 30.0)]
        for expense, price in initial_data:
            self.add_expense_to_table(expense, price)
        self.update_total()

    def add_expense(self):
        """
        Adds an expense to the expense tracker.
        This method retrieves the expense name and price from the input fields,
        validates them, and then adds the expense to the table if the inputs are valid.
        It also updates the total expense and clears the input fields.
        Raises:
            ValueError: If the price input is not a valid number.
        Shows error messages for:
            - Empty expense or price fields.
            - Invalid price input (non-numeric).
            - Negative price values.
        """
        expense = self.ui.input_panel.expense_input.text().strip()
        price = self.ui.input_panel.price_input.text().strip()

        if not expense or not price:
            self.show_error_message("Both fields are required.")
            return
        try:
            price = float(price)
        except ValueError:
            self.show_error_message("Price must be a valid number.")
            return

        if price < 0:
            self.show_error_message("Price must be a positive number.")
            return

        self.add_expense_to_table(expense, price)
        self.clear_input_fields()
        self.update_total()

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Input Error")
        msg_box.exec_()
    def update_total(self):
        total = self.calculate_total()
        self.ui.total_panel.update_total(total)

    def add_expense_to_table(self, expense, price):
        self.ui.expense_table.add_expense(expense, str(price))

    def clear_input_fields(self):
        self.ui.input_panel.expense_input.clear()
        self.ui.input_panel.price_input.clear()

    def is_valid_expense(self, expense, price):
        return expense and price

    def calculate_total(self):
        total = 0.0
        for row in range(self.ui.expense_table.rowCount()):
            item = self.ui.expense_table.item(row, 1)
            if item:
                total += float(item.text())
        return total

    def delete_expense(self, row):
        """
        Delete an expense from the expense table and update the total expense amount.

        Args:
            row (int): The row index of the expense to be deleted.
        """
        self.ui.expense_table.removeRow(row)
        self.update_total()
