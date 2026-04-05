#!/usr/bin/env python

import decimal

"""Linear function calculator"""


def linear_function_calculator(x):
    m = input("Enter your slope: ")
    slope = decimal.Decimal(m)
    y = input("Enter your y-intercept: ")
    y_intercept = decimal.Decimal(y)
    print(f"The result is: {slope} * {x} + {y_intercept} = {slope * x + y_intercept}")
    return slope * x + y_intercept


"""Non linear function calculator"""


def all_functions_calculator(function):
    x = input("Enter your x value (leave blank for 0): ")
    if x:
        x = decimal.Decimal(x)
    else:
        x = 0
    result = eval(function)
    print(f"The result is: {result}")
    return result


"""Area of a function calculator"""


def area_of_function_calculator_linear(a, b, function):
    x = float(a)
    y_a = eval(function)
    x = float(b)
    y_b = eval(function)
    a_val = decimal.Decimal(str(a))
    b_val = decimal.Decimal(str(b))
    y_a_dec = decimal.Decimal(str(y_a))
    y_b_dec = decimal.Decimal(str(y_b))
    area = (b_val - a_val) * (y_a_dec + y_b_dec) / 2
    return area


"""Area of a function calculator_non_linear"""


def area_of_function_calculator_non_linear(a, b, function):
    jump = decimal.Decimal(0.1)
    x = decimal.Decimal(a)
    b = decimal.Decimal(b)
    total = decimal.Decimal(0)
    while x <= b:
        y = eval(
            function
        )  # isn't allowed to be overriden with function = eval(function)
        total += y * jump
        x += jump
    return total


if __name__ == "__main__":
    while True:
        inp = input(
            "Enter '1' for linear function or '2' for all functions '3' for guessing the area of a function '4' for calculating the area of a linear function: "
        )
        if inp == "1":
            x = input("Enter your x value: ")
            print(linear_function_calculator(decimal.Decimal(x)))
        elif inp == "2":
            result = input("Enter your function: ")
            print(all_functions_calculator(result))
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
            # Fixed: Use numerical integration instead of trying to eval without x defined
            # This approach works for linear functions just like the non-linear function
            function = input(
                "Enter your function (use 'x' as variable, e.g., 2*x + 3): "
            )
            a = input("Enter your starting value: ")
            b = input("Enter your ending value: ")
            # Note: We don't need to eval here - the function does that internally
            print(
                f"The area under the function is {area_of_function_calculator_linear(a, b, function)}"
            )
        elif inp == "5":
            break
        else:
            print("Invalid input")
