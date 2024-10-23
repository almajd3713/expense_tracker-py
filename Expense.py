# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from app.ExpenseUI import (ExpenseUI)  # Import the UI from the new file

class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 300)

        # Create the UI and set it as the central widget
        self.ui = ExpenseUI()
        self.setCentralWidget(self.ui)

        # Set the menu bar from the UI
        self.setMenuBar(self.ui.menu_bar)

        # Connect the "Add Expense" button to the logic
        self.ui.add_button.clicked.connect(self.add_expense)

        # Initialize the table with some default data
        self.ui.table.setRowCount(3)
        initial_data = [("Veg", 40.0), ("Fruit", 70.0), ("Fuel", 60.0)]
        for row, (expense, price) in enumerate(initial_data):
            self.ui.table.setItem(row, 0, QTableWidgetItem(expense))
            self.ui.table.setItem(row, 1, QTableWidgetItem(str(price)))

        # Update the total
        self.update_total()

    def add_expense(self):
        # Get values from input fields
        expense_name = self.ui.expense_input.text().strip()
        price_text = self.ui.price_input.text().strip()

        # Add a new row to the table
        row_position = self.ui.table.rowCount()
        self.ui.table.insertRow(row_position)
        self.ui.table.setItem(row_position, 0, QTableWidgetItem(expense_name))
        self.ui.table.setItem(row_position, 1, QTableWidgetItem(price_text))

        # Clear the input fields
        self.ui.expense_input.clear()
        self.ui.price_input.clear()

        # Update the total
        self.update_total()

    def update_total(self):
        # Calculate the total price
        total = 0.0
        for row in range(self.ui.table.rowCount()):
            price_item = self.ui.table.item(row, 1)
            if price_item:
                total += float(price_item.text())
        self.ui.total_value.setText(f"{total:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())