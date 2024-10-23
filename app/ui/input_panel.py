# ui/input_panel.py
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

class InputPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Create layout
        self.layout = QHBoxLayout(self)

        # Create and configure input fields
        self.expense_label = QLabel("Expense:")
        self.expense_input = QLineEdit()
        self.expense_input.setFixedWidth(150)

        self.price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        self.price_input.setFixedWidth(100)

        # Create Add Expense button
        self.add_button = QPushButton("Add Expense")

        # Add widgets to layout
        self.layout.addWidget(self.expense_label)
        self.layout.addWidget(self.expense_input)
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(self.add_button)