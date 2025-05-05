# CalculusAlgorithm.py
import sympy as sp
import numpy as np

class CalculusParser:
    @staticmethod
    def _validate_variable(function_str, variable):
        try:
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            if not func.free_symbols:
                return True
            return var in func.free_symbols
        except Exception as e:
            return False

    @staticmethod
    def compute_derivative(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"
            
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            derivative = sp.diff(func, var)
            return derivative
        except Exception as e:
            return f"Error computing derivative: {str(e)}"

    @staticmethod
    def compute_integral(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"
            
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            integral = sp.integrate(func, var)
            return integral
        except Exception as e:
            return f"Error computing integral: {str(e)}"

    @staticmethod
    def compute_limit(function_str, variable, point):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"
            
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            limit = sp.limit(func, var, float(point))
            return limit
        except Exception as e:
            return f"Error computing limit: {str(e)}"

    @staticmethod
    def find_extrema(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"
            
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            derivative = sp.diff(func, var)
            critical_points = sp.solve(derivative, var)
            second_derivative = sp.diff(derivative, var)
            extrema = []
            for point in critical_points:
                second_deriv_value = second_derivative.subs(var, point)
                if second_deriv_value > 0:
                    extrema.append(f"Local minimum at {variable} = {point}")
                elif second_deriv_value < 0:
                    extrema.append(f"Local maximum at {variable} = {point}")
                else:
                    extrema.append(f"Possible extremum at {variable} = {point} (second derivative test inconclusive)")
            return "\n".join(extrema) if extrema else "No extrema found"
        except Exception as e:
            return f"Error finding extrema: {str(e)}"

    @staticmethod
    def solve_equation(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"
            
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            solutions = sp.solve(func, var)
            if not solutions:
                return "No solutions found"
            return "\n".join([f"{variable} = {sol}" for sol in solutions])
        except Exception as e:
            return f"Error solving equation: {str(e)}"

    @staticmethod
    def generate_variable_table(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"
            
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            derivative = sp.diff(func, var)
            
            # Find critical points (where derivative = 0 or undefined)
            critical_points = sp.solve(derivative, var)
            critical_points = [float(pt) for pt in critical_points if pt.is_real]
            critical_points.sort()
            
            # Include domain boundaries (e.g., -∞, +∞) and critical points
            points = [-float('inf')] + critical_points + [float('inf')]
            
            # Analyze behavior in each interval
            table = [f"Bảng biến thiên cho f({variable})"]
            table.append("-" * 40)
            table.append(f"{variable}    | {' | '.join([f'{pt:.2f}' if isinstance(pt, (int, float)) else str(pt) for pt in points])}")
            table.append("-" * 40)
            
            # Derivative sign (monotonicity)
            derivative_signs = []
            for i in range(len(points) - 1):
                test_point = (points[i] + points[i+1]) / 2 if points[i] != -float('inf') and points[i+1] != float('inf') else points[i] + 1 if points[i] != -float('inf') else points[i+1] - 1
                deriv_value = derivative.subs(var, test_point)
                try:
                    sign = '+' if deriv_value > 0 else '-' if deriv_value < 0 else '0'
                except (TypeError, ValueError):
                    sign = 'undefined'
                derivative_signs.append(sign)
            table.append(f"f'({variable}) | {' | '.join([' ' * 10 + sign for sign in derivative_signs])}")
            
            # Function behavior (increasing/decreasing)
            behavior = []
            for sign in derivative_signs:
                if sign == '+':
                    behavior.append('↑')
                elif sign == '-':
                    behavior.append('↓')
                else:
                    behavior.append('-')
            table.append(f"f({variable})  | {' | '.join([' ' * 10 + b for b in behavior])}")
            
            # Function values at critical points
            if critical_points:
                values = []
                for pt in critical_points:
                    try:
                        val = func.subs(var, pt)
                        values.append(f"{val:.2f}")
                    except (ValueError, TypeError):
                        values.append("undefined")
                table.append(f"Values | {' | '.join([f'({pt:.2f}, {val})' for pt, val in zip(critical_points, values)])}")
            
            return "\n".join(table)
        except Exception as e:
            return f"Error generating variable table: {str(e)}"

    def parse_calculus(self, function_str, operation, variable=None, point=None):
        try:
            if operation == "Derivative":
                return self.compute_derivative(function_str, variable)
            elif operation == "Integral":
                return self.compute_integral(function_str, variable)
            elif operation == "Limit":
                return self.compute_limit(function_str, variable, point)
            elif operation == "Find Extrema":
                return self.find_extrema(function_str, variable)
            elif operation == "Solve Equation":
                return self.solve_equation(function_str, variable)
            elif operation == "Variable Table":
                return self.generate_variable_table(function_str, variable)
            else:
                return "Unsupported calculus operation"
        except Exception as e:
            return f"Error in calculus computation: {str(e)}"