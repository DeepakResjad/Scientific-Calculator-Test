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
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def log_function(x):
    validate_numeric_input(x)
    if x <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers")
    return math.log(x)

def exp_function(x):
    validate_numeric_input(x)
    return math.exp(x)

def display_menu():
    print("Scientific Calculator")
    print("=====================")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    print("4. Square Root (sqrt)")
    print("5. Logarithm (log)")
    print("6. Exponential (exp)")
    print("7. Exit")
    print("8. End")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-8): ")
        
        if choice in {"7", "8"}:  # Allow both "Exit" and "End" to terminate
            print("Exiting calculator. Goodbye!")
            break
        
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid option. Please try again.")
            continue

        try:
            num = float(input("Enter a number: "))
            if choice == "1":
                print(f"sin({num}) = {sin_function(num)}")
            elif choice == "2":
                print(f"cos({num}) = {cos_function(num)}")
            elif choice == "3":
                print(f"tan({num}) = {tan_function(num)}")
            elif choice == "4":
                print(f"sqrt({num}) = {sqrt_function(num)}")
            elif choice == "5":
                print(f"log({num}) = {log_function(num)}")
            elif choice == "6":
                print(f"exp({num}) = {exp_function(num)}")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
