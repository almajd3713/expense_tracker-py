import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from app.db import DB
from app.ui.expense_ui import ExpenseUI
from app.ui.expense_report import ExpenseReport  # Import the new class

db_url = "./app/db/expense.db"

class ExpenseApp(QMainWindow):
    data = list()

    def __init__(self):
        super().__init__()
        # Set up the database
        self.db = DB(db_url)

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 400)
        self.center()

        # Create the UI and set it as the central widget
        self.ui = ExpenseUI()
        self.setCentralWidget(self.ui)

        # Initialize ExpenseReport with the table widget
        self.expense_report = ExpenseReport(self.ui.expense_table)

        # Connect the button to the add_expense method
        self.ui.input_panel.add_button.clicked.connect(self.add_expense)

        # Connect the row_deleted signal to the delete_expense method
        self.ui.expense_table.row_deleted.connect(self.delete_expense)
        self.ui.rows_per_page_input.textChanged.connect(self.update_rows_per_page)
        self.ui.prev_button.clicked.connect(self.ui.expense_table.prev_page)
        self.ui.next_button.clicked.connect(self.ui.expense_table.next_page)
        # Connect the export button to the export_to_pdf method
        self.ui.export_button.clicked.connect(self.expense_report.export_to_pdf)

        # Add existing data
        self.load_existing_data()

    def update_rows_per_page(self):
        try:
            rows = int(self.ui.rows_per_page_input.text())
        except ValueError:
            rows = 10  # Default value
        self.ui.expense_table.set_rows_per_page(rows)

    def center(self):
        """Center the window on the screen."""
        frame = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def load_existing_data(self):
        self.data = self.db.get_all_expenses()
        for _, expense, price, dateCreated, dateUpdated in self.data:
            self.add_expense_to_table(expense, price, dateCreated)
        self.update_total()

    def add_expense(self):
        """Adds an expense to the tracker with validation."""
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
        row = self.db.add_expense(expense, price, "") # REMOVE
        self.data.append(row)
        self.add_expense_to_table(expense, price, row[3]) # REMOVE
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

    def add_expense_to_table(self, expense, price, dateCreated):
        self.ui.expense_table.add_expense(expense, str(price), dateCreated)

    def clear_input_fields(self):
        self.ui.input_panel.expense_input.clear()
        self.ui.input_panel.price_input.clear()

    def calculate_total(self):
        total = 0.0
        for row in range(self.ui.expense_table.rowCount()):
            item = self.ui.expense_table.item(row, 1)
            if item:
                total += float(item.text())
        return total

    def delete_expense(self, row):
        """Delete an expense from the table and database."""
        row_tuple = self.data[row]
        row_tuple_id = row_tuple[0]

        self.data.remove(row_tuple)
        self.db.drop_expense(row_tuple_id)
        self.ui.expense_table.removeRow(row)
        self.update_total()
