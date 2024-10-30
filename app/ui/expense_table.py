from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import pyqtSignal

class ExpenseTable(QTableWidget):
    row_deleted = pyqtSignal(int)  # Signal to notify when a row is deleted

    def __init__(self):
        super().__init__()

        # Set up table with 3 columns (Expense, Price, Delete Button)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Expense", "Price", "Date Created", ""])
        self.setEditTriggers(self.NoEditTriggers)  # Prevent editing cells with no control
        # Pagination attributes
        self.current_page = 0
        self.rows_per_page = 10
        self.data = []
    def add_expense(self, expense, price, dateCreated):
        self.data.append((expense, price,dateCreated))
        self.update_table()

    def update_table(self):
        self.setRowCount(0)  # Clear the table
        start = self.current_page * self.rows_per_page
        end = start + self.rows_per_page
        for expense, price,dateCreated in self.data[start:end]:
            row_position = self.rowCount()
            self.insertRow(row_position)
            self.setItem(row_position, 0, QTableWidgetItem(expense))
            self.setItem(row_position, 1, QTableWidgetItem(price))
            self.setItem(row_position, 2, QTableWidgetItem(dateCreated))
            # Add delete button
            delete_button = QPushButton("Delete")
            delete_button.setObjectName("deleteButton")
            delete_button.clicked.connect(lambda _, row=row_position: self.delete_row(row))
            # delete_button.clicked.connect(lambda: self.delete_expense(delete_button))
            self.setCellWidget(row_position, 3, delete_button)
            print(f"Added expense delete button row {row_position}")



    def delete_row(self, row):
        self.data.pop(row + self.current_page * self.rows_per_page)
        self.row_deleted.emit(row)
        self.update_table()

    def set_rows_per_page(self, rows):
        self.rows_per_page = rows
        self.update_table()

    def next_page(self):
        if (self.current_page + 1) * self.rows_per_page < len(self.data):
            self.current_page += 1
            self.update_table()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_table()