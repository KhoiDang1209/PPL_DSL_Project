# CalculusAlgorithm.py
import sympy as sp
import numpy as np
from tabulate import tabulate
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
            rows = []
            for i in range(len(points) - 1):
                interval = f"({points[i]:.2f}, {points[i + 1]:.2f})" if points[i] != -float('inf') and points[i + 1] != float('inf') else "(-∞, ∞)"
                test_point = (points[i] + points[i + 1]) / 2 if points[i] != -float('inf') and points[i + 1] != float('inf') else points[i] + 1 if points[i] != -float('inf') else points[i + 1] - 1
                deriv_value = derivative.subs(var, test_point)
                try:
                    if deriv_value > 0:
                        sign = '+'
                        arrow = '↑'
                        color = '#4CAF50'  # Green
                        behavior = 'Increasing'
                    elif deriv_value < 0:
                        sign = '-'
                        arrow = '↓'
                        color = '#F44336'  # Red
                        behavior = 'Decreasing'
                    else:
                        sign = '0'
                        arrow = '→'
                        color = '#888888'  # Gray
                        behavior = 'Constant'
                except (TypeError, ValueError):
                    sign = 'undefined'
                    arrow = '?'
                    color = '#888888'
                    behavior = 'Undefined'
                rows.append((interval, sign, arrow, behavior, color))

            # Add critical points and function values
            crit_rows = []
            if critical_points:
                for pt in critical_points:
                    try:
                        val = func.subs(var, pt)
                        crit_rows.append((f"<b>Critical Point: {pt:.2f}</b>", "-", f"f({variable}) = <b>{val:.2f}</b>"))
                    except (ValueError, TypeError):
                        crit_rows.append((f"<b>Critical Point: {pt:.2f}</b>", "-", "undefined"))

            # Generate HTML table
            html = """
            <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; font-size:14px;">
                <tr style="background-color:#f2f2f2;">
                    <th>Interval</th>
                    <th>f'(x) Sign</th>
                    <th>Behavior</th>
                </tr>
            """
            for interval, sign, arrow, behavior, color in rows:
                html += f'<tr><td>{interval}</td><td style="color:{color}; font-weight:bold;">{sign} {arrow}</td><td style="color:{color};">{behavior}</td></tr>'
            for crit in crit_rows:
                html += f'<tr style="background-color:#ffe082;"><td colspan=\"3\">{crit[0]} &nbsp; {crit[2]}</td></tr>'
            html += "</table>"
            return html
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