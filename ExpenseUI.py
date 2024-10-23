# expense_ui.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QLineEdit, QLabel, QPushButton,
    QMenuBar, QMenu
)

class ExpenseUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main layout
        self.layout = QVBoxLayout(self)

        # Create a menu bar (for demonstration purposes, it will be set externally)
        self.menu_bar = QMenuBar()
        self.file_menu = QMenu("File", self)
        self.edit_menu = QMenu("Edit", self)
        self.help_menu = QMenu("Help", self)
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.edit_menu)
        self.menu_bar.addMenu(self.help_menu)

        # Create the top panel for input fields and buttons
        self.top_panel = QHBoxLayout()
        self.layout.addLayout(self.top_panel)

        # Create labels and input fields for "Expense" and "Price"
        self.expense_label = QLabel("Expense:")
        self.expense_input = QLineEdit()
        self.expense_input.setFixedWidth(150)

        self.price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        self.price_input.setFixedWidth(100)

        # Create the "Add Expense" button
        self.add_button = QPushButton("Add Expense")

        # Add the widgets to the top panel
        self.top_panel.addWidget(self.expense_label)
        self.top_panel.addWidget(self.expense_input)
        self.top_panel.addWidget(self.price_label)
        self.top_panel.addWidget(self.price_input)
        self.top_panel.addWidget(self.add_button)

        # Create the table for displaying expenses
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Expense", "Price"])
        self.layout.addWidget(self.table)

        # Create the bottom panel for displaying the total
        self.total_label = QLabel("Total:")
        self.total_value = QLabel("0.00")
        self.total_layout = QHBoxLayout()
        self.total_layout.addWidget(self.total_label)
        self.total_layout.addWidget(self.total_value)
        self.layout.addLayout(self.total_layout)