#!/usr/bin/env python

import decimal


def linear_function_calculator(x):
    """Calculates y = mx + b given user input for slope (m) and y-intercept (b)."""
    m = input("Enter your slope: ")
    slope = decimal.Decimal(m)
    y = input("Enter your y-intercept: ")
    y_intercept = decimal.Decimal(y)
    return slope * x + y_intercept


def all_functions_calculator(function):
    """Evaluates an arbitrary mathematical function string."""
    x = input("Enter your x value (leave blank for 0): ")
    if x:
        x = decimal.Decimal(x)
    else:
        x = 0

    # Note: eval() executes strings as code and is generally unsafe for untrusted input
    result = eval(function)
    return result


def area_of_function_calculator_linear(a, b, function):
    """Calculates the exact area under a linear function using the trapezoidal rule."""
    x = float(a)
    y_a = eval(function)
    x = float(b)
    y_b = eval(function)

    a_val = decimal.Decimal(str(a))
    b_val = decimal.Decimal(str(b))
    y_a_dec = decimal.Decimal(str(y_a))
    y_b_dec = decimal.Decimal(str(y_b))

    # Area of a trapezoid: (base * (height1 + height2)) / 2
    area = (b_val - a_val) * (y_a_dec + y_b_dec) / 2
    return area


def area_of_function_calculator_non_linear(a, b, function):
    """Estimates the area under a non-linear function using a Riemann sum."""
    jump = decimal.Decimal("0.1")  # Step size for the estimation
    x = decimal.Decimal(a)
    b = decimal.Decimal(b)
    total = decimal.Decimal(0)

    # Accumulate the area of rectangles for each step
    while x <= b:
        y = eval(function)
        total += y * jump
        x += jump
    return total


if __name__ == "__main__":
    # Main interactive CLI loop
    while True:
        inp = input(
            "Enter '1' for linear function or '2' for all functions '3' for guessing the area of a function '4' for calculating the area of a linear function '5' to exit: "
        )
        if inp == "1":
            x = input("Enter your x value: ")
            print(f"The Output is: {linear_function_calculator(decimal.Decimal(x))}")

        elif inp == "2":
            result = input("Enter your function: ")
            print(f"The Output is: {all_functions_calculator(result)}")

        elif inp == "3":
            function = input(
                "Enter your function (use 'x' as variable, e.g., 2*x**3): "
            )
            a = input("Enter your starting value: ")
            b = input("Enter your ending value: ")
            print(
                f"The area under the function is {area_of_function_calculator_non_linear(a, b, function)}"
            )

        elif inp == "4":
            function = input(
                "Enter your function (use 'x' as variable, e.g., 2*x + 3): "
            )
            a = input("Enter your starting value: ")
            b = input("Enter your ending value: ")
            print(
                f"The area under the function is {area_of_function_calculator_linear(a, b, function)}"
            )

        elif inp == "5":
            break

        else:
            print("Invalid input")
