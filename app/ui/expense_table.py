from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import pyqtSignal

class ExpenseTable(QTableWidget):
    row_deleted = pyqtSignal(int)  # Signal to notify when a row is deleted

    def __init__(self):
        super().__init__()

        # Set up table with 3 columns (Expense, Price, Delete Button)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Expense", "Price", ""])

    def add_expense(self, expense, price):
        """Add a new expense to the table."""
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(expense))
        self.setItem(row_position, 1, QTableWidgetItem(price))

        # Add delete button
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_expense(delete_button))
        self.setCellWidget(row_position, 2, delete_button)
        print(f"Added expense delete button row {row_position}")

    def delete_expense(self, button):
        """Emit signal to delete the row containing the button."""
        index = self.indexAt(button.pos())
        print(f"Deleting row {index.row()}")
        if index.isValid():
            self.row_deleted.emit(index.row())