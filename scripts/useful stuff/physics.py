import math
from decimal import Decimal as D, getcontext
from fractions import Fraction

getcontext().prec = 40

g = D("9.81")
PI = D("3.1415926535897932384626433832795028841971")


def sin(a):
    x = (a % 360) * PI / 180
    if x > PI:
        x -= 2 * PI
    r = t = x
    n = 1
    while abs(t) > D("1e-35"):
        t *= -(x * x) / D((2*n) * (2*n+1))
        r += t
        n += 1
    return r


def cos(a):
    return sin(a + 90)


def ask(name, unit=""):
    while True:
        try:
            v = D(input(f"{name} [{unit}]: "))
            if v.is_finite():
                return v
        except (ValueError, ArithmeticError):
            pass
        print("Invalid number.")


def show(given, formula, substitution, result, unit):
    print("\nGiven:")
    for name, value in given.items():
        print(f"  {name} = {value}")

    print("\nSolution:")
    print(formula)
    print(substitution)

    f = Fraction(result).limit_denominator(10000)
    if abs(D(f.numerator) / D(f.denominator) - result) < D("1e-30"):
        print(f"= {f}")

    print(f"= {result:.3g} {unit}")


def projectile_1():
    print("\n1. Time\n2. Impact velocity\n3. Height\n4. Initial velocity")
    c = input("Choose: ")

    if c == "1":
        h, v0 = ask("Height", "m"), ask("Initial velocity", "m/s")
        r = (-v0 + (v0**2 + 2*g*h).sqrt()) / g
        show({"h": h, "v₀": v0, "g": g}, "t = (−v₀ + √(v₀² + 2gh)) / g",
             f"t = (−{v0} + √({v0}² + 2·{g}·{h})) / {g}", r, "s")

    elif c == "2":
        v0, t = ask("Initial velocity", "m/s"), ask("Time", "s")
        r = v0 + g*t
        show({"v₀": v0, "g": g, "t": t}, "v = v₀ + gt",
             f"v = {v0} + {g}·{t}", r, "m/s")

    elif c == "3":
        v0, t = ask("Initial velocity", "m/s"), ask("Time", "s")
        r = v0*t + g*t**2/2
        show({"v₀": v0, "t": t, "g": g}, "h = v₀t + ½gt²",
             f"h = {v0}·{t} + ½·{g}·{t}²", r, "m")

    elif c == "4":
        v, t = ask("Final velocity", "m/s"), ask("Time", "s")
        r = v - g*t
        show({"v": v, "g": g, "t": t}, "v₀ = v − gt",
             f"v₀ = {v} − {g}·{t}", r, "m/s")
    else:
        print("Invalid choice.")


def projectile_2():
    options = [
        "Flight time", "Horizontal velocity", "Horizontal distance",
        "Vertical velocity", "Impact speed", "Height"
    ]
    for i, name in enumerate(options, 1):
        print(f"{i}. {name}")

    c = input("Choose: ")

    if c == "1":
        h = ask("Height", "m")
        r, given, formula, sub, unit = (2*h/g).sqrt(), {"h": h, "g": g}, \
            "t = √(2h / g)", f"t = √(2·{h} / {g})", "s"

    elif c == "2":
        x, t = ask("Horizontal distance", "m"), ask("Flight time", "s")
        r, given, formula, sub, unit = x/t, {"x": x, "t": t}, \
            "vₓ = x / t", f"vₓ = {x} / {t}", "m/s"

    elif c == "3":
        vx, t = ask("Horizontal velocity", "m/s"), ask("Flight time", "s")
        r, given, formula, sub, unit = vx*t, {"vₓ": vx, "t": t}, \
            "x = vₓ · t", f"x = {vx}·{t}", "m"

    elif c == "4":
        t = ask("Flight time", "s")
        r, given, formula, sub, unit = g*t, {"g": g, "t": t}, \
            "vᵧ = gt", f"vᵧ = {g}·{t}", "m/s"

    elif c == "5":
        vx, vy = ask("Horizontal velocity", "m/s"), ask("Vertical velocity", "m/s")
        r, given, formula, sub, unit = (vx**2 + vy**2).sqrt(), {"vₓ": vx, "vᵧ": vy}, \
            "v = √(vₓ² + vᵧ²)", f"v = √({vx}² + {vy}²)", "m/s"

    elif c == "6":
        t = ask("Flight time", "s")
        r, given, formula, sub, unit = g*t**2/2, {"g": g, "t": t}, \
            "h = ½gt²", f"h = ½·{g}·{t}²", "m"

    else:
        print("Invalid choice.")
        return

    show(given, formula, sub, r, unit)


def friction():
    options = [
        "Normal force", "Static friction", "Dynamic friction",
        "Static friction coefficient", "Dynamic friction coefficient", "Mass"
    ]
    for i, name in enumerate(options, 1):
        print(f"{i}. Calculate {name}")

    c = input("Choose: ")

    if c == "1":
        m = ask("Mass", "kg")
        r, given, formula, sub, unit = m*g, {"m": m, "g": g}, \
            "Fₙ = mg", f"Fₙ = {m}·{g}", "N"

    elif c in ("2", "3"):
        mu = ask("Friction coefficient")
        fn = ask("Normal force", "N")
        symbol = "Fₛ" if c == "2" else "Fₖ"
        coefficient = "μₛ" if c == "2" else "μₖ"
        r, given, formula, sub, unit = mu*fn, {coefficient: mu, "Fₙ": fn}, \
            f"{symbol} = {coefficient} · Fₙ", f"{symbol} = {mu}·{fn}", "N"

    elif c in ("4", "5"):
        f = ask("Static friction force" if c == "4" else "Dynamic friction force", "N")
        fn = ask("Normal force", "N")
        symbol = "μₛ" if c == "4" else "μₖ"
        force = "Fₛ" if c == "4" else "Fₖ"
        r, given, formula, sub, unit = f/fn, {force: f, "Fₙ": fn}, \
            f"{symbol} = {force} / Fₙ", f"{symbol} = {f} / {fn}", ""

    elif c == "6":
        fn = ask("Normal force", "N")
        r, given, formula, sub, unit = fn/g, {"Fₙ": fn, "g": g}, \
            "m = Fₙ / g", f"m = {fn} / {g}", "kg"

    else:
        print("Invalid choice.")
        return

    show(given, formula, sub, r, unit)


def vectors():
    print("\n1. Resultant force\n2. Resultant direction")
    print("3. Sum of horizontal forces\n4. Sum of vertical forces")
    print("5. Check equilibrium")

    c = input("Choose: ")
    if c not in ("1", "2", "3", "4", "5"):
        print("Invalid choice.")
        return

    count = int(ask("Number of forces"))
    given = {}
    fx = fy = D(0)

    for i in range(1, count + 1):
        f, a = ask(f"Force F{i}", "N"), ask(f"Angle α{i}", "°")
        fx += f*cos(a)
        fy += f*sin(a)
        given[f"F{i}"], given[f"α{i}"] = f, a

    if c == "1" or c == "5":
        r = (fx**2 + fy**2).sqrt()
        formula = "Fᵣₑₛ = √((ΣFₓ)² + (ΣFᵧ)²)"
        sub = f"Fᵣₑₛ = √(({fx})² + ({fy})²)"
        unit = "N"

    elif c == "2":
        r = D(str(math.degrees(math.atan2(float(fy), float(fx)))))
        formula, sub, unit = "α = atan2(ΣFᵧ, ΣFₓ)", f"α = atan2({fy}, {fx})", "°"

    elif c == "3":
        r = fx
        formula, sub, unit = "ΣFₓ = Σ(F · cos α)", f"ΣFₓ = {fx}", "N"

    else:
        r = fy
        formula, sub, unit = "ΣFᵧ = Σ(F · sin α)", f"ΣFᵧ = {fy}", "N"

    if c == "5":
        print("\nGiven:")
        for name, value in given.items():
            print(f"  {name} = {value}")
        print("\nSolution:")
        print(formula)
        print(sub)
        print(f"= {r:.3g} {unit}")
        print("The forces are in equilibrium." if r < D("0.001")
              else "The forces are not in equilibrium.")
    else:
        show(given | {"ΣFₓ": fx, "ΣFᵧ": fy}, formula, sub, r, unit)


def main():
    while True:
        print("\nPHYSICS CALCULATOR")
        print("1. Projectile Motion I")
        print("2. Projectile Motion II")
        print("3. Friction")
        print("4. Force Vectors")
        print("5. Crane Hook / Equilibrium")
        print("0. Exit")

        c = input("Choose a topic: ")

        if c == "1":
            projectile_1()
        elif c == "2":
            projectile_2()
        elif c == "3":
            friction()
        elif c in ("4", "5"):
            vectors()
        elif c == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
