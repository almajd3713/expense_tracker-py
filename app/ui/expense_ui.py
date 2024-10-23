# ui/expense_ui.py
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from input_panel import InputPanel
from expense_table import ExpenseTable
from menu import create_menu_bar
from total_panel import TotalPanel

class ExpenseUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create main layout
        self.layout = QVBoxLayout(self)

        # Create and add menu bar (will be set in the main window)
        self.menu_bar = create_menu_bar()

        # Create and add input panel
        self.input_panel = InputPanel()
        self.layout.addWidget(self.input_panel)

        # Create and add expense table
        self.expense_table = ExpenseTable()
        self.layout.addWidget(self.expense_table)

        # Create and add total panel
        self.total_panel = TotalPanel()
        self.layout.addWidget(self.total_panel)