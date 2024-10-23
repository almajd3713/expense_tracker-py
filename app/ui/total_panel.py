# ui/total_panel.py
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget

class TotalPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Create layout
        self.layout = QHBoxLayout(self)

        # Create total display widgets
        self.total_label = QLabel("Total:")
        self.total_value = QLabel("0.00")

        # Add widgets to layout
        self.layout.addWidget(self.total_label)
        self.layout.addWidget(self.total_value)

    def update_total(self, total):
        """Update the displayed total."""
        self.total_value.setText(f"{total:.2f}")