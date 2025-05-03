import sympy as sp
import numpy as np

class LinearAlgebraParser:
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

            augmented = A.row_join(b)
            steps = ["Step 1: Form augmented matrix [A|b]:"]
            steps.append(str(augmented))

            rref, pivots = augmented.rref()
            steps.append("Step 2: Reduced row echelon form:")
            steps.append(str(rref))

            rank_A = A.rank()
            rank_augmented = augmented.rank()
            n_vars = A.cols

            if rank_A < rank_augmented:
                steps.append("Step 3: No solution (inconsistent system)")
                return "\n".join(steps)
            elif rank_A == rank_augmented < n_vars:
                steps.append("Step 3: Infinitely many solutions (free variables exist)")
                solution = sp.linsolve((A, b))
                steps.append(f"Solution: {solution}")
            else:
                steps.append("Step 3: Unique solution")
                solution = A.LUsolve(b)
                steps.append(f"Solution: {solution}")

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

            steps = ["Step 1: Input matrix:"]
            steps.append(str(A))

            det = A.det()
            steps.append("Step 2: Compute determinant:")
            steps.append(f"Determinant = {det}")

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

            steps = ["Step 1: Input matrix:"]
            steps.append(str(A))

            det = A.det()
            steps.append("Step 2: Compute determinant:")
            steps.append(f"Determinant = {det}")
            if det == 0:
                steps.append("Step 3: Matrix is not invertible (determinant is zero)")
                return "\n".join(steps)

            inverse = A.inv()
            steps.append("Step 3: Inverse matrix:")
            steps.append(str(inverse))

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

            steps = ["Step 1: Input matrix:"]
            steps.append(str(A))

            eigenvalues = A.eigenvals()
            steps.append("Step 2: Eigenvalues (with multiplicities):")
            steps.append(str(eigenvalues))

            eigenvectors = A.eigenvects()
            steps.append("Step 3: Eigenvectors:")
            for eigenvalue, multiplicity, vectors in eigenvectors:
                steps.append(f"Eigenvalue {eigenvalue} (multiplicity {multiplicity}):")
                for vec in vectors:
                    steps.append(f"Eigenvector: {vec}")

            return "\n".join(steps)
        except Exception as e:
            return f"Error computing eigenvalues/vectors: {str(e)}"

    def parse_linear_algebra(self, operation, matrix=None, constants=None):
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
            else:
                return "Unsupported linear algebra operation"
        except Exception as e:
            return f"Error in linear algebra computation: {str(e)}"