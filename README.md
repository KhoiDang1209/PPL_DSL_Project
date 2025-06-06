# Math DSL Processor

A powerful mathematical expression processor that supports both Calculus and Linear Algebra operations using a Domain Specific Language (DSL).

## Features

- **Calculus Operations**
  - Derivatives
  - Integrals
  - Limits
  - Function evaluation
  - Trigonometric functions (sin, cos, tan)
  - Exponential and logarithmic functions

- **Linear Algebra Operations**
  - Matrix operations (addition, subtraction, multiplication)
  - Matrix inversion
  - Determinant calculation
  - Eigenvalue and eigenvector computation
  - System of linear equations solving

## Prerequisites

- Python 3.x
- PyQt5
- ANTLR4 (included in the project)
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python UI.py
```

2. Select operation type:
   - Calculus
   - Linear Algebra

3. Enter your mathematical expression following the syntax rules:
   - For Calculus: Use standard mathematical notation
   - For Linear Algebra: Use matrix notation [[a,b],[c,d]]

## Syntax Examples

### Calculus
```
# Derivative
derivative(x^2, x)

# Integral
integral(sin(x), x)

# Limit
limit((x^2-1)/(x-1), x, 1)

# Function evaluation
sin(pi/2)
```

### Linear Algebra
```
# Matrix addition
[[1,2],[3,4]] + [[5,6],[7,8]]

# Matrix multiplication
[[1,2],[3,4]] * [[5,6],[7,8]]

# Determinant
det([[1,2],[3,4]])
```

## Project Structure

```
├── UI.py                 # Main user interface
├── parser/              # Parser implementation
│   ├── math_evaluator.py
│   ├── Math.g4          # ANTLR4 grammar
│   └── ...
├── CalculusAlgorithm.py # Calculus operations
├── LinearAlgorithm.py   # Linear algebra operations
└── requirements.txt     # Python dependencies
```

## Error Handling

The system provides clear error messages for:
- Syntax errors
- Invalid mathematical operations
- Matrix dimension mismatches
- Invalid function arguments

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

[Add your license information here]

## Acknowledgments

- ANTLR4 for parsing capabilities
- PyQt5 for the user interface
- [Add any other acknowledgments]
