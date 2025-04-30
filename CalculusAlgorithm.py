# CalculusAlgorithm.py
import sympy as sp

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
            else:
                return "Unsupported calculus operation"
        except Exception as e:
            return f"Error in calculus computation: {str(e)}"   