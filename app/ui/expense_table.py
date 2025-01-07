from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import pyqtSignal

class ExpenseTable(QTableWidget):
    row_deleted = pyqtSignal(int)  # Signal to notify when a row is deleted

    def __init__(self):
        super().__init__()

        # Set up table with 3 columns (Expense, Price, Date Created, Delete Button)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Expense", "Price", "Date Created", ""])

    def add_expense(self, expense, price, dateCreated):
        """
        Add a new expense to the table.
        Args:
            expense (str): The name or description of the expense.
            price (str): The cost associated with the expense.
        Adds a new row to the table with the provided expense and price.
        Also adds a delete button to the row which allows the user to remove the expense.
        """
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(expense))
        self.setItem(row_position, 1, QTableWidgetItem(price))
        self.setItem(row_position, 2, QTableWidgetItem(dateCreated))

        # Add delete button
        delete_button = QPushButton("Delete")
        delete_button.setObjectName("deleteButton")
        delete_button.clicked.connect(lambda: self.delete_expense(delete_button))
        self.setCellWidget(row_position, 3, delete_button)
        # print(f"Added expense delete button row {row_position}") this was for debugging purposes

    def delete_table(self):
        self.setRowCount(0)

    def delete_expense(self, button):
        """
        Deletes an expense row from the table.

        This method emits a signal to delete the row containing the specified button.
        It determines the row index based on the button's position and emits the 
        `row_deleted` signal if the index is valid.

        Args:
            button (QPushButton): The button located in the row to be deleted.
        """
        index = self.indexAt(button.pos())
        # print(f"Deleting row {index.row()}") this was for debugging purposes
        if index.isValid():
            self.row_deleted.emit(index.row())
