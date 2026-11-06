import math
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 40

D = Decimal
g = D("9.81")
PI = D("3.1415926535897932384626433832795028841971")


def sin(angle):
    x = (angle % D(360)) * PI / D(180)

    if x > PI:
        x -= 2 * PI

    result = term = x
    n = 1

    while abs(term) > D("1e-35"):
        term *= -(x * x) / D((2 * n) * (2 * n + 1))
        result += term
        n += 1

    return result


def cos(angle):
    return sin(angle + D(90))


def sqrt(value):
    return value.sqrt()


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


def projectile_1():
    print("\nProjectile Motion I")
    print("1. Calculate time")
    print("2. Calculate impact velocity")
    print("3. Calculate height")
    print("4. Calculate initial velocity")

    choice = input("Choose the value to calculate: ")

    if choice == "1":
        h = get_input("Height", "m")
        v0 = get_input("Initial velocity", "m/s")

        result = (-v0 + sqrt(v0 ** 2 + 2 * g * h)) / g

        show(
            {"h": h, "v₀": v0, "g": g},
            "t = (−v₀ + √(v₀² + 2gh)) / g",
            f"t = (−{v0} + √({v0}² + 2·{g}·{h})) / {g}",
            result,
            "s"
        )

    elif choice == "2":
        v0 = get_input("Initial velocity", "m/s")
        t = get_input("Time", "s")

        result = v0 + g * t

        show(
            {"v₀": v0, "g": g, "t": t},
            "v = v₀ + gt",
            f"v = {v0} + {g}·{t}",
            result,
            "m/s"
        )

    elif choice == "3":
        v0 = get_input("Initial velocity", "m/s")
        t = get_input("Time", "s")

        result = v0 * t + g * t ** 2 / 2

        show(
            {"v₀": v0, "t": t, "g": g},
            "h = v₀t + ½gt²",
            f"h = {v0}·{t} + ½·{g}·{t}²",
            result,
            "m"
        )

    elif choice == "4":
        v = get_input("Final velocity", "m/s")
        t = get_input("Time", "s")

        result = v - g * t

        show(
            {"v": v, "g": g, "t": t},
            "v₀ = v − gt",
            f"v₀ = {v} − {g}·{t}",
            result,
            "m/s"
        )

    else:
        print("Invalid choice.")


def projectile_2():
    print("\nProjectile Motion II")
    print("1. Calculate flight time")
    print("2. Calculate horizontal velocity")
    print("3. Calculate horizontal distance")
    print("4. Calculate vertical velocity")
    print("5. Calculate impact speed")
    print("6. Calculate height")

    choice = input("Choose the value to calculate: ")

    if choice == "1":
        h = get_input("Height", "m")

        result = sqrt(2 * h / g)

        show(
            {"h": h, "g": g},
            "t = √(2h / g)",
            f"t = √(2·{h} / {g})",
            result,
            "s"
        )

    elif choice == "2":
        x = get_input("Horizontal distance", "m")
        t = get_input("Flight time", "s")

        result = x / t

        show(
            {"x": x, "t": t},
            "vₓ = x / t",
            f"vₓ = {x} / {t}",
            result,
            "m/s"
        )

    elif choice == "3":
        vx = get_input("Horizontal velocity", "m/s")
        t = get_input("Flight time", "s")

        result = vx * t

        show(
            {"vₓ": vx, "t": t},
            "x = vₓ · t",
            f"x = {vx}·{t}",
            result,
            "m"
        )

    elif choice == "4":
        t = get_input("Flight time", "s")

        result = g * t

        show(
            {"g": g, "t": t},
            "vᵧ = gt",
            f"vᵧ = {g}·{t}",
            result,
            "m/s"
        )

    elif choice == "5":
        vx = get_input("Horizontal velocity", "m/s")
        vy = get_input("Vertical velocity", "m/s")

        result = sqrt(vx ** 2 + vy ** 2)

        show(
            {"vₓ": vx, "vᵧ": vy},
            "v = √(vₓ² + vᵧ²)",
            f"v = √({vx}² + {vy}²)",
            result,
            "m/s"
        )

    elif choice == "6":
        t = get_input("Flight time", "s")

        result = g * t ** 2 / 2

        show(
            {"g": g, "t": t},
            "h = ½gt²",
            f"h = ½·{g}·{t}²",
            result,
            "m"
        )

    else:
        print("Invalid choice.")


def friction():
    print("\nFriction")
    print("1. Calculate normal force")
    print("2. Calculate static friction")
    print("3. Calculate dynamic friction")
    print("4. Calculate static friction coefficient")
    print("5. Calculate dynamic friction coefficient")
    print("6. Calculate mass")

    choice = input("Choose the value to calculate: ")

    if choice == "1":
        m = get_input("Mass", "kg")

        result = m * g

        show(
            {"m": m, "g": g},
            "Fₙ = mg",
            f"Fₙ = {m}·{g}",
            result,
            "N"
        )

    elif choice == "2":
        mu = get_input("Static friction coefficient", "")
        fn = get_input("Normal force", "N")

        result = mu * fn

        show(
            {"μₛ": mu, "Fₙ": fn},
            "Fₛ = μₛ · Fₙ",
            f"Fₛ = {mu}·{fn}",
            result,
            "N"
        )

    elif choice == "3":
        mu = get_input("Dynamic friction coefficient", "")
        fn = get_input("Normal force", "N")

        result = mu * fn

        show(
            {"μₖ": mu, "Fₙ": fn},
            "Fₖ = μₖ · Fₙ",
            f"Fₖ = {mu}·{fn}",
            result,
            "N"
        )

    elif choice == "4":
        fs = get_input("Static friction force", "N")
        fn = get_input("Normal force", "N")

        result = fs / fn

        show(
            {"Fₛ": fs, "Fₙ": fn},
            "μₛ = Fₛ / Fₙ",
            f"μₛ = {fs} / {fn}",
            result,
            ""
        )

    elif choice == "5":
        fk = get_input("Dynamic friction force", "N")
        fn = get_input("Normal force", "N")

        result = fk / fn

        show(
            {"Fₖ": fk, "Fₙ": fn},
            "μₖ = Fₖ / Fₙ",
            f"μₖ = {fk} / {fn}",
            result,
            ""
        )

    elif choice == "6":
        fn = get_input("Normal force", "N")

        result = fn / g

        show(
            {"Fₙ": fn, "g": g},
            "m = Fₙ / g",
            f"m = {fn} / {g}",
            result,
            "kg"
        )

    else:
        print("Invalid choice.")


def vector_calculator():
    print("\nForce Vectors")
    print("1. Calculate resultant force")
    print("2. Calculate resultant direction")
    print("3. Calculate sum of horizontal forces")
    print("4. Calculate sum of vertical forces")
    print("5. Check equilibrium")

    choice = input("Choose the value to calculate: ")

    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice.")
        return

    count = int(get_input("Number of forces", ""))

    fx_total = D(0)
    fy_total = D(0)
    given = {}

    for i in range(1, count + 1):
        force = get_input(f"Force F{i}", "N")
        angle = get_input(f"Angle α{i}", "°")

        fx = force * cos(angle)
        fy = force * sin(angle)

        fx_total += fx
        fy_total += fy

        given[f"F{i}"] = force
        given[f"α{i}"] = angle

    if choice == "1":
        result = sqrt(fx_total ** 2 + fy_total ** 2)

        show(
            given | {"ΣFₓ": fx_total, "ΣFᵧ": fy_total},
            "Fᵣₑₛ = √((ΣFₓ)² + (ΣFᵧ)²)",
            f"Fᵣₑₛ = √(({fx_total})² + ({fy_total})²)",
            result,
            "N"
        )

    elif choice == "2":
        result = D(str(math.degrees(math.atan2(float(fy_total), float(fx_total)))))

        show(
            given | {"ΣFₓ": fx_total, "ΣFᵧ": fy_total},
            "α = atan2(ΣFᵧ, ΣFₓ)",
            f"α = atan2({fy_total}, {fx_total})",
            result,
            "°"
        )

    elif choice == "3":
        show(
            given,
            "ΣFₓ = Σ(F · cos α)",
            f"ΣFₓ = {fx_total}",
            fx_total,
            "N"
        )

    elif choice == "4":
        show(
            given,
            "ΣFᵧ = Σ(F · sin α)",
            f"ΣFᵧ = {fy_total}",
            fy_total,
            "N"
        )

    elif choice == "5":
        result = sqrt(fx_total ** 2 + fy_total ** 2)

        print("\nGiven:")
        for name, value in given.items():
            print(f"  {name} = {value}")

        print("\nSolution:")
        print("Fᵣₑₛ = √((ΣFₓ)² + (ΣFᵧ)²)")
        print(f"Fᵣₑₛ = √(({fx_total})² + ({fy_total})²)")
        print(f"Fᵣₑₛ = {result:.3g} N")

        if result < D("0.001"):
            print("The forces are in equilibrium.")
        else:
            print("The forces are not in equilibrium.")


def main():
    while True:
        print("\n==============================")
        print("      PHYSICS CALCULATOR")
        print("==============================")
        print("1. Projectile Motion I")
        print("2. Projectile Motion II")
        print("3. Friction")
        print("4. Force Vectors")
        print("5. Crane Hook / Equilibrium")
        print("0. Exit")

        choice = input("\nChoose a topic: ")

        if choice == "1":
            projectile_1()

        elif choice == "2":
            projectile_2()

        elif choice == "3":
            friction()

        elif choice == "4":
            vector_calculator()

        elif choice == "5":
            vector_calculator()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
