# CalculusAlgorithm.py
import sympy as sp
import numpy as np
from tabulate import tabulate

class CalculusParser:
    @staticmethod
    def _format_step(step_number, title, content):
        """Helper method to format a step with consistent styling"""
        return f"\nStep {step_number}: {title}\n{content}\n"

    @staticmethod
    def _validate_variable(function_str, variable):
        try:
            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            return var in func.free_symbols
        except Exception:
            return False

    @staticmethod
    def compute_derivative(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"

            steps = []
            steps.append(CalculusParser._format_step(1, "Input function:", function_str))

            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            derivative = sp.diff(func, var)
            steps.append(CalculusParser._format_step(2, "Derivative:", str(derivative)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error computing derivative: {str(e)}"

    @staticmethod
    def compute_integral(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"

            steps = []
            steps.append(CalculusParser._format_step(1, "Input function:", function_str))

            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            integral = sp.integrate(func, var)
            steps.append(CalculusParser._format_step(2, "Integral:", str(integral)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error computing integral: {str(e)}"

    @staticmethod
    def compute_limit(function_str, variable, point):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"

            steps = []
            steps.append(CalculusParser._format_step(1, "Input function:", function_str))
            steps.append(CalculusParser._format_step(2, "Limit point:", point))

            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            try:
                point_val = float(point)
            except ValueError:
                if point.lower() == 'inf':
                    point_val = sp.oo
                elif point.lower() == '-inf':
                    point_val = -sp.oo
                else:
                    return "Error: Invalid limit point"

            limit = sp.limit(func, var, point_val)
            steps.append(CalculusParser._format_step(3, "Limit:", str(limit)))

            return "\n".join(steps)
        except Exception as e:
            return f"Error computing limit: {str(e)}"

    @staticmethod
    def find_extrema(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"

            steps = []
            steps.append(CalculusParser._format_step(1, "Input function:", function_str))

            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            derivative = sp.diff(func, var)
            steps.append(CalculusParser._format_step(2, "First derivative:", str(derivative)))

            critical_points = sp.solve(derivative, var)
            steps.append(CalculusParser._format_step(3, "Critical points:", 
                "\n".join([f"{variable} = {point}" for point in critical_points])))

            second_derivative = sp.diff(derivative, var)
            steps.append(CalculusParser._format_step(4, "Second derivative:", str(second_derivative)))

            extrema_analysis = []
            for point in critical_points:
                if point.is_real:
                    second_deriv_value = second_derivative.subs(var, point)
                    if second_deriv_value > 0:
                        extrema_analysis.append(f"Local minimum at {variable} = {point}")
                    elif second_deriv_value < 0:
                        extrema_analysis.append(f"Local maximum at {variable} = {point}")
                    else:
                        extrema_analysis.append(f"Possible inflection point at {variable} = {point}")

            steps.append(CalculusParser._format_step(5, "Extrema analysis:", 
                "\n".join(extrema_analysis) if extrema_analysis else "No real extrema found"))

            return "\n".join(steps)
        except Exception as e:
            return f"Error finding extrema: {str(e)}"

    @staticmethod
    def solve_equation(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"

            steps = []
            steps.append(CalculusParser._format_step(1, "Input equation:", function_str))

            var = sp.Symbol(variable)
            func = sp.sympify(function_str)
            solutions = sp.solve(func, var)
            
            if not solutions:
                steps.append(CalculusParser._format_step(2, "Solution:", "No solutions found"))
            else:
                steps.append(CalculusParser._format_step(2, "Solutions:", 
                    "\n".join([f"{variable} = {sol}" for sol in solutions])))

            return "\n".join(steps)
        except Exception as e:
            return f"Error solving equation: {str(e)}"

    @staticmethod
    def generate_variable_table(function_str, variable):
        try:
            if not CalculusParser._validate_variable(function_str, variable):
                return f"Error: Variable '{variable}' not found in function '{function_str}'"

            steps = []
            steps.append(CalculusParser._format_step(1, "Input function:", function_str))

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
            rows = []
            for i in range(len(points) - 1):
                interval_start = points[i]
                interval_end = points[i + 1]
                
                # Test point in the middle of the interval
                if interval_start == -float('inf'):
                    test_point = interval_end - 1
                elif interval_end == float('inf'):
                    test_point = interval_start + 1
                else:
                    test_point = (interval_start + interval_end) / 2
                
                # Evaluate derivative at test point
                deriv_value = derivative.subs(var, test_point)
                
                # Determine behavior
                if deriv_value > 0:
                    behavior = "Increasing"
                elif deriv_value < 0:
                    behavior = "Decreasing"
                else:
                    behavior = "Constant"
                
                # Format interval
                if interval_start == -float('inf'):
                    interval_str = f"(-∞, {interval_end})"
                elif interval_end == float('inf'):
                    interval_str = f"({interval_start}, ∞)"
                else:
                    interval_str = f"({interval_start}, {interval_end})"
                
                rows.append(f"Interval: {interval_str} | Behavior: {behavior}")

            steps.append(CalculusParser._format_step(2, "Function analysis:", 
                "\n".join(rows)))

            return "\n".join(steps)
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