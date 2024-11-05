import math

def validate_numeric_input(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Numeric input required")

def sin_function(x):
    validate_numeric_input(x)
    return math.sin(math.radians(x))

def cos_function(x):
    validate_numeric_input(x)
    return math.cos(math.radians(x))

def tan_function(x):
    validate_numeric_input(x)
    return math.tan(math.radians(x))

def sqrt_function(x):
    validate_numeric_input(x)
    if x < 0:
        raise ValueError("Cannot calculate square root")
    return math.sqrt(x)

def log_function(x):
    validate_numeric_input(x)
    if x <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers")
    return math.log(x)

def exp_function(x):
    validate_numeric_input(x)
    return math.exp(x)

def asin_function(x):
    validate_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("Input out of domain (must be between -1 and 1)")
    return math.degrees(math.asin(x))

def acos_function(x):
    validate_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("Input out of domain (must be between -1 and 1)")
    return math.degrees(math.acos(x))

def atan_function(x):
    validate_numeric_input(x)
    return math.degrees(math.atan(x))

def sinh_function(x):
    validate_numeric_input(x)
    return math.sinh(x)

def cosh_function(x):
    validate_numeric_input(x)
    return math.cosh(x)

def tanh_function(x):
    validate_numeric_input(x)
    return math.tanh(x)
