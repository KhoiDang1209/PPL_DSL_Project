import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QGridLayout,
                             QGroupBox, QFrame, QMessageBox, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPalette, QColor

from CalculusAlgorithm import CalculusParser
from LinearAlgorithm import LinearAlgebraParser
from math_evaluator import evaluate_expression


class MathDSLApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Math DSL Processor")
        self.setMinimumSize(1920, 1200)
        self.resize(1920, 1200)

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

        # Set object names for the GroupBoxes to style them specifically
        self.linear_algebra_operation_group.setObjectName("linear_algebra_group")
        self.constants_group.setObjectName("constants_group")
        self.calculus_operation_group.setObjectName("calculus_group")
        self.function_group.setObjectName("function_group")
        self.limit_point_group.setObjectName("limit_point_group")
        self.matrix_group.setObjectName("matrix_group")

        # Update stylesheet for no borders, custom arrow, and larger font
        stylesheet = """
        QLineEdit, QTextEdit, QComboBox {
            background-color: white;
            border-radius: 15px;
            border: 1px solid #ccc;
            padding: 5px;
            font-size: 20px;
            font-family: 'Consolas', 'Courier New', monospace;
        }
        QLabel {
            font-size: 20px;
            font-family: 'Consolas', 'Courier New', monospace;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding-left: 10px;
            padding-top: 5px;
            font-size: 20px;
            font-weight: bold;
            font-family: 'Consolas', 'Courier New', monospace;
        }
        QComboBox::drop-down {
            border: none;
        }
        QWidget#calculus_group, QWidget#linear_algebra_group {
            border-radius: 15px;
            border: none;
            background-color: white;
            margin-top: 8px;
            padding: 10px;
        }
        QGroupBox {
            border: none;
            background-color: white;
            margin-top: 0px;
            padding: 5px;
        }
        QGroupBox#function_group, QGroupBox#variable_group, QGroupBox#limit_point_group, QGroupBox#matrix_group, QGroupBox#constants_group {
            border-radius: 15px;
            border: none;
            background-color: white;
            margin-top: 8px;
            padding: 10px;
        }
        QFrame#input_frame, QFrame#output_frame {
            background-color: white;
            border-radius: 15px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        QTextEdit#result_text {
            background-color: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 15px;
            padding: 15px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 18px;
            line-height: 1.5;
            color: #212529;
        }
        QTextEdit#result_text:focus {
            border: 2px solid #3E3A9C;
        }
        QPushButton {
            font-family: 'Consolas', 'Courier New', monospace;
        }
        """
        self.setStyleSheet(stylesheet)

        # Add a Unicode arrow to the QComboBox items (workaround for lack of ::after in Qt)
        self.calculus_operation_combo.setEditable(True)
        self.calculus_operation_combo.lineEdit().setReadOnly(True)
        self.calculus_operation_combo.lineEdit().setAlignment(Qt.AlignLeft)
        self.calculus_operation_combo.lineEdit().setText(self.calculus_operation_combo.currentText() + "  ▼")
        self.calculus_operation_combo.setEditable(False)
        self.linear_algebra_operation_combo.setEditable(True)
        self.linear_algebra_operation_combo.lineEdit().setReadOnly(True)
        self.linear_algebra_operation_combo.lineEdit().setAlignment(Qt.AlignLeft)
        self.linear_algebra_operation_combo.lineEdit().setText(self.linear_algebra_operation_combo.currentText() + "  ▼")
        self.linear_algebra_operation_combo.setEditable(False)

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
        button_font = QFont("Segoe UI", 12)
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

        # Calculus Operation Selection (QWidget instead of QGroupBox)
        self.calculus_operation_group = QWidget()
        self.calculus_operation_group.setObjectName("calculus_group")
        calculus_layout = QVBoxLayout(self.calculus_operation_group)
        calculus_label = QLabel("Calculus Operation")
        calculus_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.calculus_operation_combo = QComboBox()
        self.calculus_operation_combo.addItems(
            ["Derivative", "Integral", "Limit", "Extrema", "Solve Equation", "Generate Variable Table"])
        calculus_layout.addWidget(calculus_label)
        calculus_layout.addWidget(self.calculus_operation_combo)
        input_layout.addWidget(self.calculus_operation_group)
        input_layout.addSpacing(10)

        # Linear Algebra Operation Selection (QWidget instead of QGroupBox)
        self.linear_algebra_operation_group = QWidget()
        self.linear_algebra_operation_group.setObjectName("linear_algebra_group")
        linear_algebra_layout = QVBoxLayout(self.linear_algebra_operation_group)
        linear_algebra_label = QLabel("Linear Algebra Operation")
        linear_algebra_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.linear_algebra_operation_combo = QComboBox()
        self.linear_algebra_operation_combo.addItems([
            "Inverse", "Determinant",
            "Solve Linear System", "Eigenvalues and Eigenvectors",
            "Matrices Calculation", "Diagonalize Matrix"
        ])
        linear_algebra_layout.addWidget(linear_algebra_label)
        linear_algebra_layout.addWidget(self.linear_algebra_operation_combo)
        input_layout.addWidget(self.linear_algebra_operation_group)
        input_layout.addSpacing(10)

        # Function Label and Group
        self.function_label = QLabel("Function")
        self.function_label.setFont(QFont("Segoe UI", 20, QFont.Normal))
        input_layout.addWidget(self.function_label)
        self.function_group = QGroupBox()
        self.function_group.setObjectName("function_group")
        function_layout = QVBoxLayout(self.function_group)
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Enter function (e.g., x^2 + sin(x))")
        self.function_input.setFixedSize(400, 32)
        function_layout.addWidget(self.function_input)
        input_layout.addWidget(self.function_group)
        input_layout.addSpacing(5)

        # Variable Label and Group
        self.variable_label = QLabel("Variable")
        self.variable_label.setFont(QFont("Segoe UI", 20, QFont.Normal))
        input_layout.addWidget(self.variable_label)
        self.variable_group = QGroupBox()
        self.variable_group.setObjectName("variable_group")
        variable_layout = QVBoxLayout(self.variable_group)
        self.variable_input = QLineEdit()
        self.variable_input.setPlaceholderText("Enter variable (e.g., x)")
        self.variable_input.setFixedSize(400, 32)
        variable_layout.addWidget(self.variable_input)
        input_layout.addWidget(self.variable_group)
        input_layout.addSpacing(5)

        # Limit Point Label and Group
        self.limit_point_label = QLabel("Limit Point")
        self.limit_point_label.setFont(QFont("Segoe UI", 20, QFont.Normal))
        input_layout.addWidget(self.limit_point_label)
        self.limit_point_group = QGroupBox()
        self.limit_point_group.setObjectName("limit_point_group")
        limit_layout = QVBoxLayout(self.limit_point_group)
        self.limit_point_input = QLineEdit()
        self.limit_point_input.setPlaceholderText("Enter limit point (e.g., 0)")
        self.limit_point_input.setFixedSize(400, 32)
        limit_layout.addWidget(self.limit_point_input)
        input_layout.addWidget(self.limit_point_group)
        input_layout.addSpacing(5)
        self.limit_point_group.hide()  # Hide by default

        # Matrix Input
        self.matrix_group = QGroupBox()
        self.matrix_group.setObjectName("matrix_group")
        matrix_main_layout = QVBoxLayout(self.matrix_group)
        matrix_label = QLabel("Matrix Input")
        matrix_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        matrix_main_layout.addWidget(matrix_label)
        self.matrix_layout = QVBoxLayout()
        matrix_main_layout.addLayout(self.matrix_layout)
        input_layout.addWidget(self.matrix_group)
        input_layout.addSpacing(5)

        # Constants Input for Linear System
        self.constants_group = QGroupBox()
        self.constants_group.setObjectName("constants_group")
        constants_layout = QVBoxLayout(self.constants_group)
        constants_label = QLabel("Constants (b vector)")
        constants_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        constants_layout.addWidget(constants_label)
        self.constants_input_layout = QHBoxLayout()
        constants_layout.addLayout(self.constants_input_layout)
        input_layout.addWidget(self.constants_group)
        input_layout.addSpacing(10)

        # Calculate Button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFont(QFont("Segoe UI", 12))
        input_layout.addWidget(self.calculate_button)
        combo_font = QFont("Segoe UI", 11)
        self.calculate_button.setStyleSheet("""
            background-color: #3E3A9C;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 5px;
        """)
        self.calculus_operation_combo.setFont(combo_font)
        self.linear_algebra_operation_combo.setFont(combo_font)
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
        self.function_label.show()
        self.function_group.show()
        self.variable_label.show()
        self.variable_group.show()
        self.limit_point_label.show()
        self.limit_point_group.show()
        self.matrix_group.hide()
        self.constants_group.hide()
        # Clean up matrix input
        if hasattr(self, 'matrix_input'):
            self.matrix_input.hide()
        if hasattr(self, 'second_matrix_input'):
            self.second_matrix_input.hide()
        if hasattr(self, 'matrix_operation_combo'):
            self.matrix_operation_combo.hide()
        self.update_ui_for_calculus_operation()

    def show_linear_algebra_ui(self):
        self.calculus_operation_group.hide()
        self.linear_algebra_operation_group.show()
        self.function_label.hide()
        self.function_group.hide()
        self.variable_label.hide()
        self.variable_group.hide()
        self.limit_point_label.hide()
        self.limit_point_group.hide()
        self.matrix_group.show()
        self.constants_group.show()
        # Initialize matrix input if it doesn't exist
        if not hasattr(self, 'matrices_layout'):
            self.matrices_layout = QHBoxLayout()
            self.matrix_layout.addLayout(self.matrices_layout)
        if not hasattr(self, 'matrix_input'):
            self.matrix_input = QLineEdit()
            self.matrix_input.setPlaceholderText(
                "Enter matrix rows separated by [], values separated by spaces or commas.\nExample: [[1, 0], [0, 1]]"
            )
            self.matrix_input.setFixedSize(700, 32)
            self.matrices_layout.addWidget(self.matrix_input)
        self.matrix_input.show()
        self.update_ui_for_linear_algebra_operation()
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
        self.result_text.setObjectName("result_text")  # Add object name for styling
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Result will be displayed here...")
        self.result_text.setMinimumHeight(400)  # Set minimum height for better visibility

        output_layout.addWidget(self.result_text)

    def update_ui_for_operation_type(self):
        # This method is no longer needed since buttons are used to switch between Calculus and Linear Algebra.
        # You can safely remove this method or leave it empty if not used elsewhere.
        pass

    def update_ui_for_calculus_operation(self):
        calculus_operation = self.calculus_operation_combo.currentText()
        # Show/hide limit point input for Limit operation
        if calculus_operation == "Limit":
            self.limit_point_label.show()
            self.limit_point_group.show()
        else:
            self.limit_point_label.hide()
            self.limit_point_group.hide()
        # No need for force layout update, as each group is now separate

    def update_ui_for_linear_algebra_operation(self):
        linear_algebra_operation = self.linear_algebra_operation_combo.currentText()

        # Create a horizontal layout for matrices and operation if it doesn't exist
        if not hasattr(self, 'matrices_layout'):
            self.matrices_layout = QHBoxLayout()
            self.matrix_layout.addLayout(self.matrices_layout)

        # First matrix input (needed for all operations)
        if not hasattr(self, 'matrix_input'):
            self.matrix_input = QLineEdit()
            self.matrix_input.setPlaceholderText(
                "Enter matrix rows separated by [], values separated by spaces or commas.\nExample: [[1, 0], [0, 1]]"
            )
            self.matrix_input.setFixedSize(700, 32)
            self.matrices_layout.addWidget(self.matrix_input)

        # Show/hide second matrix input and operation selector based on operation
        if linear_algebra_operation == "Matrices Calculation":
            # Operation selector
            if not hasattr(self, 'matrix_operation_combo'):
                self.matrix_operation_combo = QComboBox()
                self.matrix_operation_combo.addItems(['+', '-', '*', '/'])
                self.matrix_operation_combo.setFixedSize(50, 32)
                self.matrices_layout.addWidget(self.matrix_operation_combo, alignment=Qt.AlignCenter)

            # Second matrix input
            if not hasattr(self, 'second_matrix_input'):
                self.second_matrix_input = QLineEdit()
                self.second_matrix_input.setPlaceholderText(
                    "Enter second matrix rows separated by [], values separated by spaces or commas.\nExample: [[1, 0], [0, 1]]"
                )
                self.second_matrix_input.setFixedSize(700, 32)
                self.matrices_layout.addWidget(self.second_matrix_input)

            self.matrices_layout.setSpacing(10)  # Add some spacing between elements
            self.matrices_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

            # Show all elements
            self.matrix_input.show()
            self.matrix_operation_combo.show()
            self.second_matrix_input.show()
        else:
            # For other operations, only show the first matrix input
            self.matrix_input.show()
            if hasattr(self, 'matrix_operation_combo'):
                self.matrix_operation_combo.hide()
            if hasattr(self, 'second_matrix_input'):
                self.second_matrix_input.hide()

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
                if item.layout():
                    while item.layout().count():
                        sub_item = item.layout().takeAt(0)
                        if sub_item.widget():
                            sub_item.widget().deleteLater()
                elif item.widget():
                    item.widget().deleteLater()

        # Clear any existing matrices layout
        if hasattr(self, 'matrices_layout'):
            while self.matrices_layout.count():
                item = self.matrices_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.matrices_layout.deleteLater()
            delattr(self, 'matrices_layout')

        # Clear any existing matrix inputs
        if hasattr(self, 'matrix_input'):
            self.matrix_input.deleteLater()
            delattr(self, 'matrix_input')
        if hasattr(self, 'second_matrix_input'):
            self.second_matrix_input.deleteLater()
            delattr(self, 'second_matrix_input')
        if hasattr(self, 'matrix_operation_combo'):
            self.matrix_operation_combo.deleteLater()
            delattr(self, 'matrix_operation_combo')

    def clear_matrix(self):
        # Clear the matrix layout and inputs
        if hasattr(self, 'matrix_layout'):
            while self.matrix_layout.count():
                item = self.matrix_layout.takeAt(0)
                if item.layout():
                    while item.layout().count():
                        sub_item = item.layout().takeAt(0)
                        if sub_item.widget():
                            sub_item.widget().deleteLater()
                elif item.widget():
                    item.widget().deleteLater()

        # Clear any existing matrices layout
        if hasattr(self, 'matrices_layout'):
            while self.matrices_layout.count():
                item = self.matrices_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.matrices_layout.deleteLater()
            delattr(self, 'matrices_layout')

        # Clear any existing matrix inputs
        if hasattr(self, 'matrix_input'):
            self.matrix_input.deleteLater()
            delattr(self, 'matrix_input')
        if hasattr(self, 'second_matrix_input'):
            self.second_matrix_input.deleteLater()
            delattr(self, 'second_matrix_input')
        if hasattr(self, 'matrix_operation_combo'):
            self.matrix_operation_combo.deleteLater()
            delattr(self, 'matrix_operation_combo')

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
        self.constants_input.setFixedSize(400, 32)  # Match the size of other input fields
        self.constants_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #ccc;
                padding: 5px;
            }
        """)
        self.constants_input_layout.addWidget(self.constants_input, alignment=Qt.AlignLeft)

    def get_matrix_values(self):
        # Convert matrix input to string format for math evaluator
        matrix_values = []
        for row in self.matrix_inputs:
            row_values = []
            for input_field in row:
                value = input_field.text().strip()
                if value:
                    row_values.append(value)
            if row_values:
                matrix_values.append(row_values)
        
        # Convert to string format that math evaluator can parse
        matrix_str = "["
        for i, row in enumerate(matrix_values):
            matrix_str += "["
            matrix_str += ",".join(row)
            matrix_str += "]"
            if i < len(matrix_values) - 1:
                matrix_str += ","
        matrix_str += "]"
        
        return matrix_str

    def get_constants_values(self):
        if not hasattr(self, 'constants_input'):
            return None
            
        constants_str = self.constants_input.text().strip()
        if not constants_str:
            return None
            
        try:
            # Split by commas and convert to float
            constants = [float(x.strip()) for x in constants_str.split(',')]
            return constants
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid constant values. Please enter numeric values separated by commas (e.g., 1, 2, 3)")
            return None

    def calculate(self):
        try:
            if self.calculus_operation_group.isVisible():
                self.calculate_calculus()
            elif self.linear_algebra_operation_group.isVisible():
                self.calculate_linear_algebra()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.result_text.setText("")

    def calculate_calculus(self):
        try:
            function_str = self.function_input.text().strip()
            variable = self.variable_input.text().strip()
            
            if not function_str:
                self.result_text.setText("Error: Please enter a function")
                return
                
            if not variable:
                self.result_text.setText("Error: Please enter a variable")
                return
            
            # First validate the function using math evaluator
            try:
                # Test if the function is valid by evaluating it
                evaluate_expression(function_str)
            except Exception as e:
                error_msg = str(e)
                self.result_text.setText(f"Grammar Error:\n{error_msg}")
                QMessageBox.warning(self, "Invalid Function", f"Invalid function expression:\n{error_msg}")
                return

            operation = self.calculus_operation_combo.currentText()
            
            if operation == "Derivative":
                result = self.compute_derivative(function_str, variable)
            elif operation == "Integral":
                result = self.compute_integral(function_str, variable)
            elif operation == "Limit":
                point = self.limit_point_input.text().strip()
                if not point:
                    self.result_text.setText("Error: Please enter a limit point")
                    return
                result = self.compute_limit(function_str, variable, point)
            elif operation == "Extrema":
                result = self.find_extrema(function_str, variable)
            elif operation == "Solve Equation":
                result = self.solve_equation(function_str, variable)
            elif operation == "Generate Variable Table":
                result = self.generate_variable_table(function_str, variable)
            
            self.result_text.setText(str(result))
            
        except Exception as e:
            error_msg = str(e)
            self.result_text.setText(f"Error:\n{error_msg}")
            QMessageBox.critical(self, "Error", f"An error occurred:\n{error_msg}")

    def calculate_linear_algebra(self):
        try:
            operation = self.linear_algebra_operation_combo.currentText()
            matrix_str = self.matrix_input.text().strip()
            print(f"Matrix input from UI: '{matrix_str}'")  # Debug print
            matrix = None
            matrix_parse_error = None
            try:
                matrix = evaluate_expression(matrix_str)
            except Exception as e:
                matrix_parse_error = str(e)
                QMessageBox.warning(self, "Matrix Parse Warning", f"Matrix input had a parse error: {str(e)}\nAttempting to process anyway.")
                # Optionally, try to salvage or fallback here
                # For now, just continue with matrix=None
            result = None  # Initialize result

            if matrix is not None:
                if operation == "Inverse":
                    result = self.compute_inverse(matrix)
                elif operation == "Determinant":
                    result = self.compute_determinant(matrix)
                elif operation == "Solve Linear System":
                    constants = self.get_constants_values()
                    result = self.solve_linear_system(matrix, constants)
                elif operation == "Eigenvalues and Eigenvectors":
                    result = self.compute_eigenvalues_vectors(matrix)
                elif operation == "Matrices Calculation":
                    matrix2_str = self.get_second_matrix_values()
                    try:
                        matrix2 = evaluate_expression(matrix2_str)
                    except Exception as e:
                        QMessageBox.warning(self, "Invalid Matrix", f"Invalid second matrix expression: {str(e)}")
                        return
                    operation_type = self.matrix_operation_combo.currentText()
                    if operation_type == '+':
                        result = self.add_matrices(matrix, matrix2)
                    elif operation_type == '-':
                        result = self.subtract_matrices(matrix, matrix2)
                    elif operation_type == '*':
                        result = self.multiply_matrices(matrix, matrix2)
                    elif operation_type == '/':
                        result = self.divide_matrices(matrix, matrix2)
                elif operation == "Diagonalize Matrix":
                    result = self.diagonalize_matrix(matrix)
            else:
                result = "Matrix input could not be parsed. Please check your input."

            if result is not None:
                if matrix_parse_error:
                    self.result_text.setText(f"[Warning: {matrix_parse_error}]\n{str(result)}")
                else:
                    self.result_text.setText(str(result))
            else:
                self.result_text.setText("No result (operation not recognized or failed).")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def compute_derivative(self, func, variable):
        return CalculusParser.compute_derivative(func, variable)

    def compute_integral(self, func, variable):
        return CalculusParser.compute_integral(func, variable)

    def compute_limit(self, func, variable, point):
        return CalculusParser.compute_limit(func, variable, point)

    def find_extrema(self, func, variable):
        return CalculusParser.find_extrema(func, variable)

    def solve_equation(self, function_str, variable):
        return CalculusParser.solve_equation(function_str, variable)

    def generate_variable_table(self, function_str, variable):
        return CalculusParser.generate_variable_table(function_str, variable)

    def solve_linear_system(self, matrix, constants):
        return LinearAlgebraParser.solve_linear_system(matrix, constants)

    def compute_determinant(self, matrix):
        return LinearAlgebraParser.compute_determinant(matrix)

    def compute_inverse(self, matrix):
        return LinearAlgebraParser.compute_inverse(matrix)

    def compute_eigenvalues_vectors(self, matrix):
        return LinearAlgebraParser.compute_eigenvalues_vectors(matrix)

    def add_matrices(self, matrix1, matrix2):
        return LinearAlgebraParser.add_matrices(matrix1, matrix2)

    def subtract_matrices(self, matrix1, matrix2):
        return LinearAlgebraParser.subtract_matrices(matrix1, matrix2)

    def multiply_matrices(self, matrix1, matrix2):
        return LinearAlgebraParser.multiply_matrices(matrix1, matrix2)

    def divide_matrices(self, matrix1, matrix2):
        return LinearAlgebraParser.divide_matrices(matrix1, matrix2)

    def diagonalize_matrix(self, matrix):
        return LinearAlgebraParser.diagonalize_matrix(matrix)

    def get_second_matrix_values(self):
        if hasattr(self, 'second_matrix_input'):
            matrix_str = self.second_matrix_input.text().strip()
            print(f"Second matrix input from UI: '{matrix_str}'")  # Debug print
            return matrix_str
        return ""


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