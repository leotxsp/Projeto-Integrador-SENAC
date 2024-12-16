from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView

# Create a sample application
app = QApplication([])

# Create a QWidget to hold the QTableWidget
window = QWidget()
layout = QVBoxLayout(window)

# Create a QTableWidget
table_widget = QTableWidget(5, 3)  # 5 rows and 3 columns

# Set the stylesheet for the QTableWidget
table_widget.setStyleSheet("""
    QTableWidget {
        border: 1px solid #ccc; /* Border around the table */
        gridline-color: #aaa; /* Color of the grid lines */
        background-color: #f9f9f9; /* Background color of the table */
        alternate-background-color: #f1f1f1; /* Alternate row color */
        selection-background-color: #0078d7; /* Background color for selected rows */
        selection-color: white; /* Text color for selected rows */
        font-size: 14px; /* Font size */
    }

    QTableWidget::item {
        padding: 10px; /* Padding for each item */
        border: 1px solid #ddd; /* Border for each item */
    }

    QTableWidget::item:selected {
        background-color: #0078d7; /* Background color for selected items */
        color: white; /* Text color for selected items */
    }

    QHeaderView::section {
        background-color: #0078d7; /* Header background color */
        color: white; /* Header text color */
        padding: 10px; /* Padding for header */
        border: 1px solid #aaa; /* Border for header */
    }
""")

# Populate the table with some sample data
for row in range(5):
    for column in range(3):
        item = QTableWidgetItem(f"Item {row + 1}, {column + 1}")
        table_widget.setItem(row, column, item)

# Set the header to stretch the last section
header = table_widget.horizontalHeader()
header.setStretchLastSection(True)  # Make the last column stretch to fill the space

# Optionally, set the initial column widths
table_widget.setColumnWidth(0, 100)  # Set width for the first column
table_widget.setColumnWidth(1, 100)  # Set width for the second column
# The last column will stretch to fill the remaining space

# Add the table widget to the layout
layout.addWidget(table_widget)

# Set the layout to the window
window.setLayout(layout)
window.setWindowTitle("Responsive QTableWidget Example")
window.resize(600, 400)
window.show()

# Run the application
app.exec()