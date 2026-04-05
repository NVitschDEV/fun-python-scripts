#!/usr/bin/env python


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


while True:
    f = input("Press 1 to continue...")
    if f == "1":
        n = input("Enter a non-negative integer: ")
        n = int(n)

        print(f"Fibonacci({n}) = {fibonacci(n)}")
    else:
        break
