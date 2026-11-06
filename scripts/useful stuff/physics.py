
import math
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 40

D = Decimal
g = D("9.81")
PI = D("3.1415926535897932384626433832795028841971")


# Decimal trigonometry
def sin(angle):
    x = (angle % D(360)) * PI / D(180)
    if x > PI:
        x -= 2 * PI

    result = term = x
    n = 1

    while abs(term) > D("1e-35"):
        term *= -(x * x) / D((2*n) * (2*n+1))
        result += term
        n += 1

    return result


def cos(angle):
    return sin(angle + D(90))


def sqrt(value):
    return value.sqrt()


# Input
def get_input(name, unit):
    while True:
        value = input(f"{name} [{unit}]: ").strip()

        try:
            number = D(value)

            if number.is_finite():
                return number

        except (ValueError, ArithmeticError):
            pass

        print("Invalid number.")


# Output
def show(given, formula, substituted, result, unit):
    print("\nGiven:")
    for name, value in given.items():
        print(f"  {name} = {value}")

    print("\nSolution:")
    print(formula)
    print(substituted)

    fraction = Fraction(result).limit_denominator(10000)

    if abs(D(fraction.numerator) / D(fraction.denominator) - result) < D("1e-30"):
        print(f"= {fraction}")

    print(f"= {result:.3g} {unit}")


# Select target
def select(options):
    print("\nWhat do you want to calculate?")

    for key, name in options.items():
        print(f"{key}. {name}")

    while True:
        choice = input("\nChoice: ").strip()

        if choice in options:
            return choice

        print("Invalid selection.")


# Exercise 1: Free fall
def projectile_1():
    choice = select({
        "1": "Time (t)",
        "2": "Impact velocity (v)",
        "3": "Height (h)",
        "4": "Initial velocity (v0)"
    })

    if choice == "1":
        h = get_input("Height", "m")
        v0 = get_input("Initial velocity downward", "m/s")

        if h < 0:
            print("Height cannot be negative.")
            return

        result = (-v0 + sqrt(v0**2 + 2*g*h)) / g

        show(
            {"h": h, "v0": v0, "g": g},
            "t = (-v0 + sqrt(v0² + 2gh)) / g",
            f"t = (-{v0} + sqrt({v0}² + 2*{g}*{h})) / {g}",
            result, "s"
        )

    elif choice == "2":
        v0 = get_input("Initial velocity", "m/s")
        t = get_input("Time", "s")

        result = v0 + g*t

        show(
            {"v0": v0, "t": t, "g": g},
            "v = v0 + g*t",
            f"v = {v0} + {g}*{t}",
            result, "m/s"
        )

    elif choice == "3":
        v0 = get_input("Initial velocity downward", "m/s")
        t = get_input("Time", "s")

        result = v0*t + g*t**2 / 2

        show(
            {"v0": v0, "t": t, "g": g},
            "h = v0*t + 1/2*g*t²",
            f"h = {v0}*{t} + 1/2*{g}*{t}²",
            result, "m"
        )

    elif choice == "4":
        v = get_input("Final velocity", "m/s")
        t = get_input("Time", "s")

        if t == 0:
            print("Time cannot be zero.")
            return

        result = v - g*t

        show(
            {"v": v, "t": t, "g": g},
            "v0 = v - g*t",
            f"v0 = {v} - {g}*{t}",
            result, "m/s"
        )


# Exercise 2: Horizontal projectile
def projectile_2():
    choice = select({
        "1": "Flight time (t)",
        "2": "Horizontal velocity (vx)",
        "3": "Horizontal distance (x)",
        "4": "Vertical velocity (vy)",
        "5": "Impact velocity (v)",
        "6": "Height (h)"
    })

    if choice == "1":
        h = get_input("Height", "m")

        if h < 0:
            print("Height cannot be negative.")
            return

        result = sqrt(2*h/g)

        show(
            {"h": h, "g": g},
            "t = sqrt(2h/g)",
            f"t = sqrt(2*{h}/{g})",
            result, "s"
        )

    elif choice == "2":
        x = get_input("Horizontal distance", "m")
        t = get_input("Flight time", "s")

        if t == 0:
            print("Time cannot be zero.")
            return

        result = x/t

        show(
            {"x": x, "t": t},
            "vx = x/t",
            f"vx = {x}/{t}",
            result, "m/s"
        )

    elif choice == "3":
        vx = get_input("Horizontal velocity", "m/s")
        t = get_input("Flight time", "s")

        result = vx*t

        show(
            {"vx": vx, "t": t},
            "x = vx*t",
            f"x = {vx}*{t}",
            result, "m"
        )

    elif choice == "4":
        t = get_input("Flight time", "s")

        result = g*t

        show(
            {"g": g, "t": t},
            "vy = g*t",
            f"vy = {g}*{t}",
            result, "m/s"
        )

    elif choice == "5":
        vx = get_input("Horizontal velocity", "m/s")
        vy = get_input("Vertical velocity", "m/s")

        result = sqrt(vx**2 + vy**2)

        show(
            {"vx": vx, "vy": vy},
            "v = sqrt(vx² + vy²)",
            f"v = sqrt({vx}² + {vy}²)",
            result, "m/s"
        )

    elif choice == "6":
        t = get_input("Flight time", "s")

        result = g*t**2/2

        show(
            {"g": g, "t": t},
            "h = 1/2*g*t²",
            f"h = 1/2*{g}*{t}²",
            result, "m"
        )


# Exercise 3: Friction
def friction():
    choice = select({
        "1": "Normal force (Fn)",
        "2": "Static friction force (Fs)",
        "3": "Dynamic friction force (Fk)",
        "4": "Static friction coefficient (μs)",
        "5": "Dynamic friction coefficient (μk)",
        "6": "Mass (m)"
    })

    if choice == "1":
        m = get_input("Mass", "kg")
        result = m*g

        show(
            {"m": m, "g": g},
            "Fn = m*g",
            f"Fn = {m}*{g}",
            result, "N"
        )

    elif choice == "2":
        mu = get_input("Static friction coefficient", "")
        fn = get_input("Normal force", "N")

        result = mu*fn

        show(
            {"μs": mu, "Fn": fn},
            "Fs = μs*Fn",
            f"Fs = {mu}*{fn}",
            result, "N"
        )

    elif choice == "3":
        mu = get_input("Dynamic friction coefficient", "")
        fn = get_input("Normal force", "N")

        result = mu*fn

        show(
            {"μk": mu, "Fn": fn},
            "Fk = μk*Fn",
            f"Fk = {mu}*{fn}",
            result, "N"
        )

    elif choice == "4":
        fs = get_input("Static friction force", "N")
        fn = get_input("Normal force", "N")

        if fn == 0:
            print("Normal force cannot be zero.")
            return

        result = fs/fn

        show(
            {"Fs": fs, "Fn": fn},
            "μs = Fs/Fn",
            f"μs = {fs}/{fn}",
            result, ""
        )

    elif choice == "5":
        fk = get_input("Dynamic friction force", "N")
        fn = get_input("Normal force", "N")

        if fn == 0:
            print("Normal force cannot be zero.")
            return

        result = fk/fn

        show(
            {"Fk": fk, "Fn": fn},
            "μk = Fk/Fn",
            f"μk = {fk}/{fn}",
            result, ""
        )

    elif choice == "6":
        fn = get_input("Normal force", "N")

        result = fn/g

        show(
            {"Fn": fn, "g": g},
            "m = Fn/g",
            f"m = {fn}/{g}",
            result, "kg"
        )


# Exercise 4 and 5: Force vectors
def vectors():
    choice = select({
        "1": "Resultant force (Fres)",
        "2": "Resultant direction (α)",
        "3": "Horizontal resultant (ΣFx)",
        "4": "Vertical resultant (ΣFy)"
    })

    count = int(input("\nNumber of forces: "))

    if not 1 <= count <= 10:
        print("Invalid number of forces.")
        return

    fx_total = D(0)
    fy_total = D(0)
    given = {}

    for i in range(count):
        print(f"\nForce F{i+1}")

        magnitude = get_input("Magnitude", "N")
        angle = get_input("Angle from positive horizontal axis", "°")

        if magnitude < 0:
            print("Magnitude cannot be negative.")
            return

        fx_total += magnitude*cos(angle)
        fy_total += magnitude*sin(angle)

        given[f"F{i+1}"] = magnitude
        given[f"α{i+1}"] = angle

    if choice == "1":
        result = sqrt(fx_total**2 + fy_total**2)

        show(
            given,
            "Fres = sqrt(ΣFx² + ΣFy²)",
            f"Fres = sqrt({fx_total}² + {fy_total}²)",
            result, "N"
        )

    elif choice == "2":
        if fx_total == 0 and fy_total == 0:
            print("Direction is undefined because the resultant is zero.")
            return

        result = D(str(math.degrees(
            math.atan2(float(fy_total), float(fx_total))
        )))

        show(
            {"ΣFx": fx_total, "ΣFy": fy_total},
            "α = atan2(ΣFy, ΣFx)",
            f"α = atan2({fy_total}, {fx_total})",
            result, "°"
        )

    elif choice == "3":
        show(
            given,
            "ΣFx = Σ(F*cos(α))",
            f"ΣFx = {fx_total}",
            fx_total, "N"
        )

    elif choice == "4":
        show(
            given,
            "ΣFy = Σ(F*sin(α))",
            f"ΣFy = {fy_total}",
            fy_total, "N"
        )

    if choice != "2":
        if fx_total == 0 and fy_total == 0:
            print("\nThe forces are in equilibrium.")
        else:
            print("\nThe forces are NOT in equilibrium.")


# Main menu
def main():
    topics = {
        "1": ("Projectile motion I", projectile_1),
        "2": ("Projectile motion II", projectile_2),
        "3": ("Friction", friction),
        "4": ("Resultant forces", vectors),
        "5": ("Equilibrium", vectors)
    }

    while True:
        print("\n=== PHYSICS CALCULATOR ===")

        for key, (name, _) in topics.items():
            print(f"{key}. {name}")

        print("Q. Quit")

        choice = input("\nSelect topic: ").lower().strip()

        if choice == "q":
            break

        if choice not in topics:
            print("Invalid selection.")
            continue

        print(f"\n=== {topics[choice][0]} ===")

        try:
            topics[choice][1]()
        except (ArithmeticError, ValueError, OverflowError) as error:
            print(f"Calculation error: {error}")

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()
