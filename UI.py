import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QGridLayout,
                             QGroupBox, QFrame, QMessageBox, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPalette, QColor

from CalculusAlgorithm import CalculusParser
from LinearAlgorithm import LinearAlgebraParser

class MathDSLApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Math DSL Processor")
        self.setMinimumSize(1440, 512)

        # Initialize main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create header
        self.setup_header()

        # Create content layout
        self.content_layout = QHBoxLayout()
        self.main_layout.addLayout(self.content_layout)

        # Create input and output sections
        self.setup_input_section()
        self.setup_output_section()

        # Add sections to the content layout
        self.content_layout.addWidget(self.input_frame)
        self.content_layout.addWidget(self.output_frame)

        # Initialize variables
        self.matrix_inputs = []
        self.constant_inputs = []

        # Connect signals
        self.connect_signals()

        # Show only Calculus UI initially
        self.show_calculus_ui()

        self.input_frame.setObjectName("input_frame")
        self.output_frame.setObjectName("output_frame")

        stylesheet = """
        QLineEdit, QTextEdit {
            background-color: white;
            border-radius: 15px;
            border: 1px solid #ccc;
            padding: 5px;
        }
        QFrame#input_frame, QFrame#output_frame {
            background-color: white;
            border-radius: 15px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        QGroupBox {
            border: none;
            background-color: white;
            padding: 5px;
        }
        
        QComboBox::drop-down {
            border: none;
        }
        QComboBox {
            background-color: white;
            border-radius: 15px;
            border: 1px solid #ccc;
            padding: 5px;
        }
        QPushButton {
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 5px;
        }
        """
        self.setStyleSheet(stylesheet)
        self.setStyleSheet(stylesheet)
    def setup_header(self):
        header_layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Math DSL Processor")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Segoe UI")
        title_font.setBold(True)
        title_font.setPointSize(18)
        title_label.setFont(title_font)

        # Subtitle label
        subtitle_label = QLabel("Perform mathematical operations using a Domain Specific Language")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_font = QFont("Segoe UI")
        subtitle_font.setPointSize(14)
        subtitle_label.setFont(subtitle_font)

        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        header_layout.addSpacing(20)

        self.main_layout.addLayout(header_layout)


    def setup_input_section(self):
        self.input_frame = QFrame()
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        input_layout = QVBoxLayout(self.input_frame)

        # Input section title
        input_title = QLabel("Input")
        input_title_font = QFont("Segoe UI")
        input_title_font.setBold(True)
        input_title_font.setPointSize(14)
        input_title.setFont(input_title_font)

        input_description = QLabel("Select operation and provide inputs")
        input_description.setFont(QFont("Segoe UI", 12))

        input_layout.addWidget(input_title)
        input_layout.addWidget(input_description)
        input_layout.addSpacing(10)

        # Operation Type Buttons
        operation_type_layout = QHBoxLayout()
        self.calculus_button = QPushButton("Calculus")
        self.linear_algebra_button = QPushButton("Linear Algebra")
        # Set font size for buttons
        button_font = QFont("Segoe UI", 12)  # Adjust font size
        self.calculus_button.setFont(button_font)
        self.linear_algebra_button.setFont(button_font)
        self.calculus_button.setStyleSheet("""
            background-color: #E2E7FF;
            color: black;
            border-radius: 10px;
            border: none;
            padding: 5px;
        """)

        self.linear_algebra_button.setStyleSheet("""
            background-color: #E2E7FF;
            color: black;
            border-radius: 10px;
            border: none;
            padding: 5px;
        """)
        operation_type_layout.addWidget(self.calculus_button)
        operation_type_layout.addWidget(self.linear_algebra_button)
        input_layout.addLayout(operation_type_layout)
        input_layout.addSpacing(10)

        # Calculus Operation Selection
        self.calculus_operation_group = QGroupBox()
        calculus_layout = QVBoxLayout(self.calculus_operation_group)
        calculus_label = QLabel("Calculus Operation")
        calculus_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.calculus_operation_combo = QComboBox()
        self.calculus_operation_combo.addItems(["Derivative", "Integral", "Limit", "Extrema"])

        calculus_layout.addWidget(calculus_label)
        calculus_layout.addWidget(self.calculus_operation_combo)
        input_layout.addWidget(self.calculus_operation_group)

        # Linear Algebra Operation Selection
        self.linear_algebra_operation_group = QGroupBox()
        linear_algebra_layout = QVBoxLayout(self.linear_algebra_operation_group)
        linear_algebra_label = QLabel("Linear Algebra Operation")
        linear_algebra_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.linear_algebra_operation_combo = QComboBox()
        self.linear_algebra_operation_combo.addItems([
            "Solve Linear System", "Determinant",
            "Inverse", "Eigenvalues and Eigenvectors"
        ])

        linear_algebra_layout.addWidget(linear_algebra_label)
        linear_algebra_layout.addWidget(self.linear_algebra_operation_combo)
        input_layout.addWidget(self.linear_algebra_operation_group)

        # Function Input
        self.function_group = QGroupBox()
        function_layout = QVBoxLayout(self.function_group)

        function_label = QLabel("Function")
        function_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.function_input = QLineEdit()
        self.function_input.setFixedSize(400,32)
        self.function_input.setPlaceholderText("Enter function (e.g., x^2 + sin(x))")

        variable_label = QLabel("Variable")
        variable_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.variable_input = QLineEdit()
        self.variable_input.setFixedSize(400,32)
        self.variable_input.setPlaceholderText("Enter variable (e.g., x)")

        function_layout.addWidget(function_label)
        function_layout.addWidget(self.function_input)
        function_layout.addWidget(variable_label)
        function_layout.addWidget(self.variable_input)

        input_layout.addWidget(self.function_group)

        # Limit Point Input
        self.limit_point_group = QGroupBox()
        limit_layout = QVBoxLayout(self.limit_point_group)

        limit_point_label = QLabel("Limit Point")
        limit_point_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.limit_point_input = QLineEdit()
        self.limit_point_input.setFixedSize(400,32)
        self.limit_point_input.setPlaceholderText("Enter limit point (e.g., 0)")

        limit_layout.addWidget(limit_point_label)
        limit_layout.addWidget(self.limit_point_input)

        input_layout.addWidget(self.limit_point_group)

        # Matrix Input
        self.matrix_group = QGroupBox()
        matrix_main_layout = QVBoxLayout(self.matrix_group)

        matrix_label = QLabel("Matrix Input")
        matrix_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        matrix_main_layout.addWidget(matrix_label)

        # Initialize matrix layout
        self.matrix_layout = QVBoxLayout()
        matrix_main_layout.addLayout(self.matrix_layout)

        input_layout.addWidget(self.matrix_group)

        # Constants Input for Linear System
        self.constants_group = QGroupBox()
        constants_layout = QVBoxLayout(self.constants_group)

        constants_label = QLabel("Constants (b vector)")
        constants_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        constants_layout.addWidget(constants_label)

        self.constants_input_layout = QHBoxLayout()
        constants_layout.addLayout(self.constants_input_layout)

        input_layout.addWidget(self.constants_group)

        # Calculate Button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFont(QFont("Segoe UI", 12))
        input_layout.addWidget(self.calculate_button)
        # Set font size for combo boxes
        combo_font = QFont("Segoe UI", 11)  # Font size 11
        self.calculate_button.setStyleSheet("""
            background-color: #3E3A9C;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 5px;
        """)
        self.calculus_operation_combo.setFont(combo_font)
        self.linear_algebra_operation_combo.setFont(combo_font)
        # Add some spacing at the bottom
        input_layout.addStretch()

    def connect_signals(self):
        self.calculus_button.clicked.connect(self.show_calculus_ui)
        self.linear_algebra_button.clicked.connect(self.show_linear_algebra_ui)
        self.calculus_operation_combo.currentTextChanged.connect(self.update_ui_for_calculus_operation)
        self.linear_algebra_operation_combo.currentTextChanged.connect(self.update_ui_for_linear_algebra_operation)


        self.calculate_button.clicked.connect(self.calculate)

    def show_calculus_ui(self):
        self.calculus_operation_group.show()
        self.linear_algebra_operation_group.hide()
        self.function_group.show()
        self.matrix_group.hide()
        self.constants_group.hide()
        self.update_ui_for_calculus_operation()

    def show_linear_algebra_ui(self):
        self.calculus_operation_group.hide()
        self.linear_algebra_operation_group.show()
        self.function_group.hide()
        self.matrix_group.show()
        self.update_ui_for_linear_algebra_operation()
        if not self.matrix_inputs:
            self.initialize_matrix(2, 2)

        self.calculate_button.clicked.connect(self.calculate)
    def setup_output_section(self):
        self.output_frame = QFrame()
        self.output_frame.setFrameShape(QFrame.StyledPanel)
        self.output_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        output_layout = QVBoxLayout(self.output_frame)

        # Output section title
        output_title = QLabel("Result")
        output_title.setFont(QFont("Segoe UI", 12))
        output_title_font = QFont()
        output_title_font.setBold(True)
        output_title_font.setPointSize(14)
        output_title.setFont(output_title_font)

        output_description = QLabel("Output of the operation")
        output_description.setFont(QFont("Segoe UI", 12))

        output_layout.addWidget(output_title)
        output_layout.addWidget(output_description)
        output_layout.addSpacing(10)

        # Result text area
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Result will be displayed here...")

        output_layout.addWidget(self.result_text)

    def update_ui_for_operation_type(self):
        # This method is no longer needed since buttons are used to switch between Calculus and Linear Algebra.
        # You can safely remove this method or leave it empty if not used elsewhere.
        pass

    def update_ui_for_calculus_operation(self):
        calculus_operation = self.calculus_operation_combo.currentText()

        # Show/hide limit point input for Limit operation
        if calculus_operation == "Limit":
            self.limit_point_group.show()
        else:
            self.limit_point_group.hide()

    def update_ui_for_linear_algebra_operation(self):
        linear_algebra_operation = self.linear_algebra_operation_combo.currentText()

        # Show matrix and constants input only for "Solve Linear System"
        if linear_algebra_operation == "Solve Linear System":
            self.matrix_group.show()
            self.constants_group.show()
            self.update_constants_inputs()
        else:
            self.constants_group.hide()

    def initialize_matrix(self, rows=None, cols=None):
        # Clear existing matrix inputs
        if hasattr(self, 'matrix_layout'):
            while self.matrix_layout.count():
                item = self.matrix_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        # Add a single text field for the entire matrix
        self.matrix_input = QLineEdit()
        self.matrix_input.setPlaceholderText(
            "Enter matrix rows separated by [], values separated by spaces or commas.\nExample: [[1, 0], [0, 1]]"
        )
        self.matrix_input.setFixedSize(400, 32)
        self.matrix_layout.addWidget(self.matrix_input)

    def clear_matrix(self):
        # Clear the matrix layout and inputs
        if hasattr(self, 'matrix_layout'):
            while self.matrix_layout.count():
                item = self.matrix_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
        self.matrix_inputs = []

    def update_constants_inputs(self):
        # Clear existing constants inputs
        while self.constants_input_layout.count():
            item = self.constants_input_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Add a single text field for constants
        self.constants_input = QLineEdit()
        self.constants_input.setPlaceholderText("Enter constants separated by commas (e.g., 1, 2, 3)")
        self.constants_input.setFixedWidth(400)
        self.constants_input.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
            border: 1px solid #ccc;
            padding: 5px;
        """)
        self.constants_input_layout.addWidget(self.constants_input, alignment=Qt.AlignLeft)

    def get_matrix_values(self):
        matrix = []
        for row in self.matrix_inputs:
            matrix_row = []
            for input_field in row:
                value = input_field.text()
                try:
                    # Try to convert to float
                    matrix_row.append(float(value) if value else 0)
                except ValueError:
                    QMessageBox.warning(self, "Input Error", "Invalid matrix value. Please enter numeric values only.")
                    return None
            matrix.append(matrix_row)
        return matrix

    def get_constants_values(self):
        constants = []
        for input_field in self.constant_inputs:
            value = input_field.text()
            try:
                # Try to convert to float
                constants.append(float(value) if value else 0)
            except ValueError:
                QMessageBox.warning(self, "Input Error", "Invalid constant value. Please enter numeric values only.")
                return None
        return constants

    def calculate(self):
        operation_type = self.operation_type_combo.currentText()

        try:
            if operation_type == "Calculus":
                self.calculate_calculus()
            else:  # Linear Algebra
                self.calculate_linear_algebra()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.result_text.setText("")

    def calculate_calculus(self):
        calculus_operation = self.calculus_operation_combo.currentText()
        function_input = self.function_input.text()
        variable_input = self.variable_input.text()

        # Validate inputs
        if not function_input or not variable_input:
            QMessageBox.warning(self, "Input Error", "Function and variable are required.")
            return

        result = ""
        if calculus_operation == "Derivative":
            result = self.compute_derivative(function_input, variable_input)
        elif calculus_operation == "Integral":
            result = self.compute_integral(function_input, variable_input)
        elif calculus_operation == "Limit":
            point_input = self.limit_point_input.text()
            if not point_input:
                QMessageBox.warning(self, "Input Error", "Limit point is required.")
                return
            result = self.compute_limit(function_input, variable_input, point_input)
        elif calculus_operation == "Extrema":
            result = self.find_extrema(function_input, variable_input)

        self.result_text.setText(result)

    def calculate_linear_algebra(self):
        linear_algebra_operation = self.linear_algebra_operation_combo.currentText()

        # Get matrix values
        matrix = self.get_matrix_values()
        if matrix is None:
            return

        result = ""
        if linear_algebra_operation == "Solve Linear System":
            # Get constants values
            constants = self.get_constants_values()
            if constants is None:
                return

            # Check dimensions
            if len(matrix) != len(constants):
                QMessageBox.warning(self, "Input Error",
                                    "The number of rows in the matrix must match the number of constants.")
                return

            result = self.solve_linear_system(matrix, constants)
        elif linear_algebra_operation == "Determinant":
            # Check if matrix is square
            rows = len(matrix)
            for row in matrix:
                if len(row) != rows:
                    QMessageBox.warning(self, "Input Error", "Matrix must be square for determinant calculation.")
                    return
            result = self.compute_determinant(matrix)
        elif linear_algebra_operation == "Inverse":
            # Check if matrix is square
            rows = len(matrix)
            for row in matrix:
                if len(row) != rows:
                    QMessageBox.warning(self, "Input Error", "Matrix must be square for inverse calculation.")
                    return
            result = self.compute_inverse(matrix)
        elif linear_algebra_operation == "Eigenvalues and Eigenvectors":
            # Check if matrix is square
            rows = len(matrix)
            for row in matrix:
                if len(row) != rows:
                    QMessageBox.warning(self, "Input Error",
                                        "Matrix must be square for eigenvalue/eigenvector calculation.")
                    return
            result = self.compute_eigenvalues_vectors(matrix)

        self.result_text.setText(result)

    def compute_derivative(self, func, variable):
        return CalculusParser.compute_derivative(func, variable)

    def compute_integral(self, func, variable):
        return CalculusParser.compute_integral(func, variable)

    def compute_limit(self, func, variable, point):
        return CalculusParser.compute_limit(func, variable, point)

    def find_extrema(self, func, variable):
        return CalculusParser.find_extrema(func, variable)

    def solve_linear_system(self, matrix, constants):
        return LinearAlgebraParser.solve_linear_system(matrix, constants)

    def compute_determinant(self, matrix):
        return LinearAlgebraParser.compute_determinant(matrix)

    def compute_inverse(self, matrix):
        return LinearAlgebraParser.compute_inverse(matrix)

    def compute_eigenvalues_vectors(self, matrix):
        return LinearAlgebraParser.compute_eigenvalues_vectors(matrix)


def apply_dark_style(app):
    # Apply dark theme
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(dark_palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Uncomment to apply dark style
    # apply_dark_style(app)

    window = MathDSLApp()
    window.show()
    sys.exit(app.exec_())