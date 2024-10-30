from PyQt5.QtWidgets import QTableWidget, QMessageBox
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Spacer

class ExpenseReport:
    def __init__(self, expense_table: QTableWidget):
        self.expense_table = expense_table

    def export_to_pdf(self):
        """Export the expense table to a PDF, excluding delete buttons."""
        pdf = SimpleDocTemplate("expense_report.pdf", pagesize=A4)

        # Extract data from the first two columns (excluding delete buttons)
        data = [["Expense", "Price"]]  # Header row
        for row in range(self.expense_table.rowCount()):
            expense = self.expense_table.item(row, 0).text()
            price = self.expense_table.item(row, 1).text()
            data.append([expense, price])

        # Create a table for the PDF
        table = Table(data, colWidths=[3 * inch, 2 * inch])

        # Style the table
        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Header background
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center align all cells
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Bold header font
            ("FONTSIZE", (0, 0), (-1, -1), 12),  # Set font size for all cells
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),  # Extra padding for header
            ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),  # Alternating row colors
        ])
        table.setStyle(style)

        # Center the table on the PDF by adding space above it
        elements = [Spacer(1, 2 * inch), table]  # Add space at the top

        # Build the PDF with the elements
        pdf.build(elements)
        QMessageBox.information(
            None, "Export Successful", "Expenses have been exported to expenses_report.pdf"
        )