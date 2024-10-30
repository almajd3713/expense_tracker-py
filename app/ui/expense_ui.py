from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSpacerItem,
    QSizePolicy, QPushButton
)
from app.ui.input_panel import InputPanel
from app.ui.expense_table import ExpenseTable
from app.ui.total_panel import TotalPanel

class ExpenseUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(10)

        # Input panel (aligned horizontally)
        self.input_panel = InputPanel()
        self.layout.addWidget(self.input_panel)

        # Spacer between the input and table
        self.layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Expense table
        self.expense_table = ExpenseTable()
        self.layout.addWidget(self.expense_table)

        # Total panel at the bottom
        self.total_panel = TotalPanel()
        self.layout.addWidget(self.total_panel)

        # Export button at the very bottom
        self.export_button = QPushButton("Export to PDF")
        self.export_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Horizontal layout for the button (in case you want more widgets later)
        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        button_layout.addWidget(self.export_button)
        button_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Add the button layout to the main layout
        self.layout.addLayout(button_layout)