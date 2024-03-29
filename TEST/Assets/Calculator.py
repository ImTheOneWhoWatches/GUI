import time
import math
import sympy as sp
import os
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Help information for arithmetic operations
def print_arithmetic_help():
    print("Arithmetic Operations:")
    print("1. Addition: Adds two numbers.")
    print("2. Subtraction: Subtracts one number from another.")
    print("3. Multiplication: Multiplies two numbers.")
    print("4. Division: Divides one number by another.")
    print("5. Modulus: Returns the remainder of division.")
    print("6. Floor Division: Returns the quotient of division, rounded down to the nearest integer.")

# Help information for algebraic operations
def print_algebra_help():
    print("Algebraic Operations:")
    print("1. Solve Linear Equation (ax + b = c): Solves linear equations of the form ax + b = c.")
    print("2. Solve Quadratic Equation (ax^2 + bx + c = 0): Solves quadratic equations of the form ax^2 + bx + c = 0.")
    print("3. Solve Cubic Equation (ax^3 + bx^2 + cx + d = 0): Solves cubic equations of the form ax^3 + bx^2 + cx + d = 0.")
    print("4. Solve Exponential Equation (a^x = b): Solves exponential equations of the form a^x = b.")
    print("5. Solve Logarithmic Equation (log_a(x) = b): Solves logarithmic equations of the form log_a(x) = b.")
    print("6. Y = MX + B: Calculates the value of y for a given linear equation y = mx + b.")
    print("7. Simplify Algebraic Expression: Simplifies algebraic expressions.")

# Help information for trigonometry operations
def print_trigonometry_help():
    print("Trigonometry Operations:")
    print("1. Sine (sin): Calculates the sine of an angle.")
    print("2. Cosine (cos): Calculates the cosine of an angle.")
    print("3. Tangent (tan): Calculates the tangent of an angle.")
    print("4. Inverse Sine (arcsin or asin): Calculates the inverse sine of a value.")
    print("5. Inverse Cosine (arccos or acos): Calculates the inverse cosine of a value.")
    print("6. Inverse Tangent (arctan or atan): Calculates the inverse tangent of a value.")
    print("7. Cosecant (csc): Calculates the cosecant of an angle.")
    print("8. Secant (sec): Calculates the secant of an angle.")
    print("9. Cotangent (cot): Calculates the cotangent of an angle.")

# Help information for mathematical operations
def print_mathematical_help():
    print("Mathematical Operations:")
    print("1. Square Root: Calculates the square root of a number.")
    print("2. Power: Raises a number to a power.")

# Print banner
def print_banner():
    print(Fore.BLUE + """
     ______ __           ____               _       __  __          _       __          __           __
    /_  __// /_   ___   / __ \  ____   ___ | |     / / / /_   ____ | |     / / ____ _  / /_  _____  / /_   ___    _____
     / /  / __ \ / _ \ / / / / / __ \ / _ \| | /| / / / __ \ / __ \| | /| / / / __ `/ / __/ / ___/ / __ \ / _ \  / ___/
    / /  / / / //  __// /_/ / / / / //  __/| |/ |/ / / / / // /_/ /| |/ |/ / / /_/ / / /_  / /__  / / / //  __/ (__  )
   /_/  /_/ /_/ \___/ \____/ /_/ /_/ \___/ |__/|__/ /_/ /_/ \____/ |__/|__/  \__,_/  \__/  \___/ /_/ /_/ \___/ /____/
""" + Style.RESET_ALL)

# Print separator
def print_separator():
    print(Fore.GREEN + "========================================================================================================================" + Style.RESET_ALL)

# Arithmetic operations
def arithmetic_operations():
    while True:
        print_separator()
        print("Arithmetic Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Floor Division")
        print("7. Clear Screen")
        print("8. Help")
        print("9. Back to main menu")

        operation = input("Enter your choice: ")

        if operation == "1": 
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            print(f"The sum of {num1} and {num2} is {num1 + num2}")
        elif operation == "2":
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            print(f"The difference between {num1} and {num2} is {num1 - num2}")
        elif operation == "3":
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            print(f"The product of {num1} and {num2} is {num1 * num2}")
        elif operation == "4":
            num1 = input_number("Enter numerator: ")
            num2 = input_number("Enter denominator: ")
            if num2 != 0:
                print(f"The result of {num1} divided by {num2} is {num1 / num2}")
            else:
                print_error("Cannot divide by zero")
        elif operation == "5":
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            print(f"The remainder of {num1} divided by {num2} is {num1 % num2}")
        elif operation == "6":
            num1 = input_number("Enter numerator: ")
            num2 = input_number("Enter denominator: ")
            if num2 != 0:
                print(f"The result of {num1} divided by {num2} (floor division) is {num1 // num2}")
            else:
                print_error("Cannot divide by zero")
        elif operation == "7":
            clear_screen()
            print_banner()
        elif operation == "8":
            print_arithmetic_help()
        elif operation == "9":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Function to handle input of numbers
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print_error("Invalid input. Please enter a valid number.")

# Function to print error messages
def print_error(message):
    print(Fore.RED + f"Error: {message}" + Style.RESET_ALL)

# Algebraic operations
def algebra_operations():
    while True:
        print_separator()
        print("Algebraic Operations:")
        print("1. Solve Linear Equation (ax + b = c)")
        print("2. Solve Quadratic Equation (ax^2 + bx + c = 0)")
        print("3. Solve Cubic Equation (ax^3 + bx^2 + cx + d = 0)")
        print("4. Solve Exponential Equation (a^x = b)")
        print("5. Solve Logarithmic Equation (log_a(x) = b)")
        print("6. Y = MX + B")
        print("7. Simplify Algebraic Expression")
        print("8. Clear")
        print("9. Help")
        print("10. Back to main menu")

        operation = input("Enter your choice: ")

        if operation == "1": 
            a = input_number("Enter the coefficient of x: ")
            b = input_number("Enter the constant term: ")
            c = input_number("Enter the constant on the right side: ")
            if a != 0:
                x = (c - b) / a
                print(f"The solution to the equation {a}x + {b} = {c} is x = {x}")
            else:
                print_error("'a' cannot be zero")
        elif operation == "2":
            a = input_number("Enter the coefficient of x^2 (a): ")
            b = input_number("Enter the coefficient of x (b): ")
            c = input_number("Enter the constant term (c): ")

            # Calculate the discriminant
            discriminant = b**2 - 4*a*c

            if a != 0:
                if discriminant > 0:
                    # Two real and distinct roots
                    root1 = (-b + math.sqrt(discriminant)) / (2*a)
                    root2 = (-b - math.sqrt(discriminant)) / (2*a)
                    print(f"The roots of the quadratic equation are: {root1} and {root2}")
                elif discriminant == 0:
                    # One real root (repeated)
                    root = -b / (2*a)
                    print(f"The root of the quadratic equation is: {root}")
                else:
                    # No real roots (complex roots)
                    real_part = -b / (2*a)
                    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
                    print(f"The roots of the quadratic equation are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
            else:
                print_error("Invalid entry")
        elif operation == "3":
            a = input_number("Enter the coefficient of x^3 (a): ")
            b = input_number("Enter the coefficient of x^2 (b): ")
            c = input_number("Enter the coefficient of x (c): ")
            d = input_number("Enter the constant term (d): ")

            # Cardano's method for solving cubic equations
            p = c / a - (b**2) / (3 * a**2)
            q = d / a - (b * c) / (3 * a**2) + (2 * b**3) / (27 * a**3)
            delta = q**2 / 4 + p**3 / 27

            if delta > 0:
                # One real root and two complex roots
                u = (-q / 2 + math.sqrt(delta))**(1/3)
                v = (-q / 2 - math.sqrt(delta))**(1/3)
                root1 = u + v - b / (3 * a)
                print(f"The real root of the cubic equation is: {root1}")
            elif delta == 0:
                # One real root (repeated)
                if q >= 0:
                    root = -2 * (q / 2)**(1/3) - b / (3 * a)
                else:
                    root = 2 * abs(q / 2)**(1/3) - b / (3 * a)
                print(f"The real root of the cubic equation is: {root}")
            else:
                # Three real roots
                t = -q / 2
                phi = math.acos(t / math.sqrt(-p**3 / 27))
                root1 = 2 * math.sqrt(-p / 3) * math.cos(phi / 3) - b / (3 * a)
                root2 = 2 * math.sqrt(-p / 3) * math.cos((phi + 2 * math.pi) / 3) - b / (3 * a)
                root3 = 2 * math.sqrt(-p / 3) * math.cos((phi + 4 * math.pi) / 3) - b / (3 * a)
                print(f"The real roots of the cubic equation are: {root1}, {root2}, and {root3}")
        elif operation == "4":
            a = input_number("Enter the base (a): ")
            b = input_number("Enter the constant term (b): ")

            if a > 0 and a != 1:  # Ensure a is positive and not equal to 1
                x = math.log(b) / math.log(a)
                print(f"The solution to the exponential equation {a}^x = {b} is x = {x}")
            else:
                print_error("Base 'a' must be positive and not equal to 1")
        elif operation == "5":
            a = input_number("Enter the base of the logarithm (a): ")
            b = input_number("Enter the constant term (b): ")

            if a > 0 and a != 1:  # Ensure a is positive and not equal to 1
                x = a ** b
                print(f"The solution to the logarithmic equation log_{a}(x) = {b} is x = {x}")
            else:
                print_error("Base 'a' must be positive and not equal to 1")
        elif operation == "6":
            m = input_number("Enter the slope (m): ")
            x = input_number("Enter the x-coordinate: ")
            b = input_number("Enter the y-intercept (b): ")

            y = m * x + b
            print(f"The value of y for the linear equation y = {m}x + {b} at x = {x} is y = {y}")
        elif operation == "7":
            expression = input("Enter the algebraic expression: ")
            simplified_expression = sp.simplify(expression)
            print(f"The simplified expression is: {simplified_expression}")
        elif operation == "8":
            clear_screen()
            print_banner()
        elif operation == "9":
            print_algebra_help()
        elif operation == "10":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Trigonometry operations
def trigonometry_operations():
    while True:
        print_separator()
        print("Trigonometry Operations:")
        print("1. Sine (sin)")
        print("2. Cosine (cos)")
        print("3. Tangent (tan)")
        print("4. Inverse Sine (arcsin or asin)")
        print("5. Inverse Cosine (arccos or acos)")
        print("6. Inverse Tangent (arctan or atan)")
        print("7. Cosecant (csc)")
        print("8. Secant (sec)")
        print("9. Cotangent (cot)")
        print("10. Help")
        print("11. Back to main menu")

        operation = input("Enter your choice: ")

        if operation in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            angle = input_number("Enter the angle in degrees: ")
            angle_rad = math.radians(angle)

            if operation == "1":
                result = math.sin(angle_rad)
                print(f"The sine of {angle} degrees is {result}")
            elif operation == "2":
                result = math.cos(angle_rad)
                print(f"The cosine of {angle} degrees is {result}")
            elif operation == "3":
                result = math.tan(angle_rad)
                print(f"The tangent of {angle} degrees is {result}")
            elif operation == "4":
                result = math.asin(angle_rad)
                print(f"The inverse sine of {angle} degrees is {result}")
            elif operation == "5":
                result = math.acos(angle_rad)
                print(f"The inverse cosine of {angle} degrees is {result}")
            elif operation == "6":
                result = math.atan(angle_rad)
                print(f"The inverse tangent of {angle} degrees is {result}")
            elif operation == "7":
                result = 1 / math.sin(angle_rad)
                print(f"The cosecant of {angle} degrees is {result}")
            elif operation == "8":
                result = 1 / math.cos(angle_rad)
                print(f"The secant of {angle} degrees is {result}")
            elif operation == "9":
                result = 1 / math.tan(angle_rad)
                print(f"The cotangent of {angle} degrees is {result}")
        elif operation == "10":
            print_trigonometry_help()
        elif operation == "11":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Mathematical operations
def mathematical_operations():
    while True:
        print_separator()
        print("Mathematical Operations:")
        print("1. Square Root")
        print("2. Power")
        print("3. Help")
        print("4. Back to main menu")

        operation = input("Enter your choice: ")

        if operation == "1":
            num = input_number("Enter a number: ")
            if num >= 0:
                result = math.sqrt(num)
                print(f"The square root of {num} is {result}")
            else:
                print_error("Cannot calculate square root of a negative number")
        elif operation == "2":
            base = input_number("Enter the base: ")
            exponent = input_number("Enter the exponent: ")
            result = base ** exponent
            print(f"{base} raised to the power of {exponent} is {result}")
        elif operation == "3":
            print_mathematical_help()
        elif operation == "4":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Main function
def main():
    while True:
        clear_screen()
        print_banner()
        print("Welcome to MathIt!, by TheOneWhoWatches")
        print_separator()
        print("Select an operation:")
        print("1. Arithmetic Operations")
        print("2. Algebraic Operations")
        print("3. Trigonometry Operations")
        print("4. Mathematical Operations")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arithmetic_operations()
        elif choice == "2":
            algebra_operations()
        elif choice == "3":
            trigonometry_operations()
        elif choice == "4":
            mathematical_operations()
        elif choice == "5":
            print("Thank you for using MathIt. Goodbye!")
            time.sleep(2)
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Run the main function
if __name__ == "__main__":
    main()