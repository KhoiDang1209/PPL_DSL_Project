import sympy as sp
import numpy as np

class LinearAlgebraParser:
    @staticmethod
    def _format_matrix_output(matrix):
        """Format matrix output to show 2 decimal places"""
        if isinstance(matrix, sp.Matrix):
            # Convert to list of lists
            matrix_list = matrix.tolist()
            # Format each element to 2 decimal places
            formatted_rows = []
            for row in matrix_list:
                formatted_row = [f"{x:.2f}" for x in row]
                formatted_rows.append(formatted_row)
            # Convert back to string representation
            rows_str = [f"[{', '.join(row)}]" for row in formatted_rows]
            return f"Matrix([{', '.join(rows_str)}])"
        return str(matrix)

    @staticmethod
    def _validate_matrix(matrix):
        try:
            if not matrix or not isinstance(matrix, list):
                return False
            if not all(isinstance(row, list) for row in matrix):
                return False
            row_length = len(matrix[0])
            return all(len(row) == row_length for row in matrix)
        except Exception:
            return False

    @staticmethod
    def _to_sympy_matrix(matrix):
        try:
            return sp.Matrix(matrix)
        except Exception as e:
            return None

    @staticmethod
    def _format_step(step_number, title, content):
        """Helper method to format a step with consistent styling"""
        return f"\nStep {step_number}: {title}\n{content}\n"

    @staticmethod
    def solve_linear_system(coefficients, constants):
        try:
            if not LinearAlgebraParser._validate_matrix(coefficients):
                return "Error: Invalid coefficient matrix"
            if not isinstance(constants, list):
                return "Error: Constants must be a list"
            if len(coefficients) != len(constants):
                return "Error: Number of equations must match number of constants"

            A = LinearAlgebraParser._to_sympy_matrix(coefficients)
            b = sp.Matrix(constants)
            if A is None or b is None:
                return "Error: Invalid matrix or vector input"

            steps = []
            augmented = A.row_join(b)
            steps.append(LinearAlgebraParser._format_step(1, "Form augmented matrix [A|b]:", 
                LinearAlgebraParser._format_matrix_output(augmented)))

            rref, pivots = augmented.rref()
            steps.append(LinearAlgebraParser._format_step(2, "Reduced row echelon form:", 
                LinearAlgebraParser._format_matrix_output(rref)))

            rank_A = A.rank()
            rank_augmented = augmented.rank()
            n_vars = A.cols

            if rank_A < rank_augmented:
                steps.append(LinearAlgebraParser._format_step(3, "Analysis:", 
                    "No solution (inconsistent system)"))
            elif rank_A == rank_augmented < n_vars:
                steps.append(LinearAlgebraParser._format_step(3, "Analysis:", 
                    "Infinitely many solutions (free variables exist)"))
                solution = sp.linsolve((A, b))
                steps.append(LinearAlgebraParser._format_step(4, "Solution:", str(solution)))
            else:
                steps.append(LinearAlgebraParser._format_step(3, "Analysis:", 
                    "Unique solution"))
                solution = A.LUsolve(b)
                steps.append(LinearAlgebraParser._format_step(4, "Solution:", 
                    LinearAlgebraParser._format_matrix_output(solution)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error solving linear system: {str(e)}"

    @staticmethod
    def compute_determinant(matrix):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix):
                return "Error: Invalid matrix"
            if len(matrix) != len(matrix[0]):
                return "Error: Matrix must be square"

            A = LinearAlgebraParser._to_sympy_matrix(matrix)
            if A is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrix:", 
                LinearAlgebraParser._format_matrix_output(A)))

            det = A.det()
            steps.append(LinearAlgebraParser._format_step(2, "Determinant:", 
                f"{det:.2f}"))

            return "\n".join(steps)
        except Exception as e:
            return f"Error computing determinant: {str(e)}"

    @staticmethod
    def compute_inverse(matrix):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix):
                return "Error: Invalid matrix"
            if len(matrix) != len(matrix[0]):
                return "Error: Matrix must be square"

            A = LinearAlgebraParser._to_sympy_matrix(matrix)
            if A is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrix:", 
                LinearAlgebraParser._format_matrix_output(A)))

            det = A.det()
            steps.append(LinearAlgebraParser._format_step(2, "Determinant:", 
                f"{det:.2f}"))
            
            if det == 0:
                steps.append(LinearAlgebraParser._format_step(3, "Analysis:", 
                    "Matrix is not invertible (determinant is zero)"))
                return "\n".join(steps)

            inverse = A.inv()
            steps.append(LinearAlgebraParser._format_step(3, "Inverse matrix:", 
                LinearAlgebraParser._format_matrix_output(inverse)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error computing inverse: {str(e)}"

    @staticmethod
    def compute_eigenvalues_vectors(matrix):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix):
                return "Error: Invalid matrix"
            if len(matrix) != len(matrix[0]):
                return "Error: Matrix must be square"

            A = LinearAlgebraParser._to_sympy_matrix(matrix)
            if A is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrix:", 
                LinearAlgebraParser._format_matrix_output(A)))

            eigenvalues = A.eigenvals()
            steps.append(LinearAlgebraParser._format_step(2, "Eigenvalues (with multiplicities):", 
                str(eigenvalues)))

            eigenvectors = A.eigenvects()
            eigenvector_text = []
            for eigenvalue, multiplicity, vectors in eigenvectors:
                eigenvector_text.append(f"Eigenvalue {eigenvalue:.2f} (multiplicity {multiplicity}):")
                for vec in vectors:
                    eigenvector_text.append(f"Eigenvector: {LinearAlgebraParser._format_matrix_output(vec)}")
            
            steps.append(LinearAlgebraParser._format_step(3, "Eigenvectors:", 
                "\n".join(eigenvector_text)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error computing eigenvalues/vectors: {str(e)}"

    @staticmethod
    def add_matrices(matrix1, matrix2):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix1) or not LinearAlgebraParser._validate_matrix(matrix2):
                return "Error: Invalid matrix input"
            if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                return "Error: Matrices must have the same dimensions"

            A = LinearAlgebraParser._to_sympy_matrix(matrix1)
            B = LinearAlgebraParser._to_sympy_matrix(matrix2)
            if A is None or B is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrices:", 
                f"Matrix A:\n{LinearAlgebraParser._format_matrix_output(A)}\n\nMatrix B:\n{LinearAlgebraParser._format_matrix_output(B)}"))

            result = A + B
            steps.append(LinearAlgebraParser._format_step(2, "Result:", 
                LinearAlgebraParser._format_matrix_output(result)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error adding matrices: {str(e)}"

    @staticmethod
    def subtract_matrices(matrix1, matrix2):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix1) or not LinearAlgebraParser._validate_matrix(matrix2):
                return "Error: Invalid matrix input"
            if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                return "Error: Matrices must have the same dimensions"

            A = LinearAlgebraParser._to_sympy_matrix(matrix1)
            B = LinearAlgebraParser._to_sympy_matrix(matrix2)
            if A is None or B is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrices:", 
                f"Matrix A:\n{LinearAlgebraParser._format_matrix_output(A)}\n\nMatrix B:\n{LinearAlgebraParser._format_matrix_output(B)}"))

            result = A - B
            steps.append(LinearAlgebraParser._format_step(2, "Result:", 
                LinearAlgebraParser._format_matrix_output(result)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error subtracting matrices: {str(e)}"

    @staticmethod
    def multiply_matrices(matrix1, matrix2):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix1) or not LinearAlgebraParser._validate_matrix(matrix2):
                return "Error: Invalid matrix input"
            if len(matrix1[0]) != len(matrix2):
                return "Error: Number of columns in first matrix must equal number of rows in second matrix"

            A = LinearAlgebraParser._to_sympy_matrix(matrix1)
            B = LinearAlgebraParser._to_sympy_matrix(matrix2)
            if A is None or B is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrices:", 
                f"Matrix A:\n{LinearAlgebraParser._format_matrix_output(A)}\n\nMatrix B:\n{LinearAlgebraParser._format_matrix_output(B)}"))

            result = A * B
            steps.append(LinearAlgebraParser._format_step(2, "Result:", 
                LinearAlgebraParser._format_matrix_output(result)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error multiplying matrices: {str(e)}"

    @staticmethod
    def divide_matrices(matrix1, matrix2):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix1) or not LinearAlgebraParser._validate_matrix(matrix2):
                return "Error: Invalid matrix input"
            if len(matrix2) != len(matrix2[0]):
                return "Error: Second matrix must be square"
            if len(matrix1[0]) != len(matrix2):
                return "Error: Number of columns in first matrix must equal number of rows in second matrix"

            A = LinearAlgebraParser._to_sympy_matrix(matrix1)
            B = LinearAlgebraParser._to_sympy_matrix(matrix2)
            if A is None or B is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrices:", 
                f"Matrix A:\n{LinearAlgebraParser._format_matrix_output(A)}\n\nMatrix B:\n{LinearAlgebraParser._format_matrix_output(B)}"))

            det = B.det()
            steps.append(LinearAlgebraParser._format_step(2, "Determinant of B:", 
                f"{det:.2f}"))
            
            if det == 0:
                steps.append(LinearAlgebraParser._format_step(3, "Analysis:", 
                    "Second matrix is not invertible (determinant is zero)"))
                return "\n".join(steps)

            B_inv = B.inv()
            steps.append(LinearAlgebraParser._format_step(3, "Inverse of B:", 
                LinearAlgebraParser._format_matrix_output(B_inv)))

            result = A * B_inv
            steps.append(LinearAlgebraParser._format_step(4, "Result (A * B^(-1)):", 
                LinearAlgebraParser._format_matrix_output(result)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error dividing matrices: {str(e)}"

    @staticmethod
    def diagonalize_matrix(matrix):
        try:
            if not LinearAlgebraParser._validate_matrix(matrix):
                return "Error: Invalid matrix"
            if len(matrix) != len(matrix[0]):
                return "Error: Matrix must be square"

            A = LinearAlgebraParser._to_sympy_matrix(matrix)
            if A is None:
                return "Error: Invalid matrix input"

            steps = []
            steps.append(LinearAlgebraParser._format_step(1, "Input matrix:", 
                LinearAlgebraParser._format_matrix_output(A)))

            try:
                P, D = A.diagonalize()
                steps.append(LinearAlgebraParser._format_step(2, "Diagonalization:", 
                    f"Matrix P (eigenvectors):\n{LinearAlgebraParser._format_matrix_output(P)}\n\n" +
                    f"Diagonal matrix D (eigenvalues):\n{LinearAlgebraParser._format_matrix_output(D)}"))
                
                steps.append(LinearAlgebraParser._format_step(3, "Verification (P^(-1)):", 
                    LinearAlgebraParser._format_matrix_output(P.inv())))
            except sp.MatrixError:
                steps.append(LinearAlgebraParser._format_step(2, "Analysis:", 
                    "Matrix is not diagonalizable"))

            return "\n".join(steps)
        except Exception as e:
            return f"Error diagonalizing matrix: {str(e)}"

    def parse_linear_algebra(self, operation, matrix=None, matrix2=None, constants=None):
        try:
            if operation == "Solve Linear System":
                if matrix is None or constants is None:
                    return "Error: Matrix and constants required for linear system"
                return self.solve_linear_system(matrix, constants)
            elif operation == "Determinant":
                if matrix is None:
                    return "Error: Matrix required for determinant"
                return self.compute_determinant(matrix)
            elif operation == "Inverse":
                if matrix is None:
                    return "Error: Matrix required for inverse"
                return self.compute_inverse(matrix)
            elif operation == "Eigenvalues and Eigenvectors":
                if matrix is None:
                    return "Error: Matrix required for eigenvalues/vectors"
                return self.compute_eigenvalues_vectors(matrix)
            elif operation == "Add Matrices":
                if matrix is None or matrix2 is None:
                    return "Error: Two matrices required for addition"
                return self.add_matrices(matrix, matrix2)
            elif operation == "Subtract Matrices":
                if matrix is None or matrix2 is None:
                    return "Error: Two matrices required for subtraction"
                return self.subtract_matrices(matrix, matrix2)
            elif operation == "Multiply Matrices":
                if matrix is None or matrix2 is None:
                    return "Error: Two matrices required for multiplication"
                return self.multiply_matrices(matrix, matrix2)
            elif operation == "Divide Matrices":
                if matrix is None or matrix2 is None:
                    return "Error: Two matrices required for division"
                return self.divide_matrices(matrix, matrix2)
            elif operation == "Diagonalize":
                if matrix is None:
                    return "Error: Matrix required for diagonalization"
                return self.diagonalize_matrix(matrix)
            else:
                return "Unsupported linear algebra operation"
        except Exception as e:
            return f"Error in linear algebra computation: {str(e)}"
