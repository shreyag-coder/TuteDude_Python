#ASSIGNMENT 3:
# Module 4: Functions & Modules in Python
# Task 1: Calculate Factorial Using a Function

import math

def factorial(n) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


# Task 2: Using the Math Module for Calculations
def math_calc(n):
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    if n == 0:
        raise ValueError("Logarithm is not defined for zero.")

    print(f"Square root: {math.sqrt(n)}")
    print(f"Logarithm: {math.log(n)}")
    print(f"Sine: {math.sin(n)}")

def main():
    try:
        value = int(input("Enter a number: "))
        print(f"Factorial of {value} is : {factorial(value)}")

        math_value = float(input("Enter a number for math calculation: "))
        math_calc(math_value)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



