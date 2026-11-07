# PHYSICS CALCULATOR
# Texas Instruments TI-Nspire CX II-T CAS
#
# Interface: Hybrid (text menus + TI System screen clearing)
# Precision: Python floating-point, with fraction display when a
#             result is sufficiently close to a simple fraction.
#
# Transfer this file into a TI-Nspire Python document.
# The TI Python editor may require pasting the contents into a
# new Python page in a .tns document.

import math
import ti_system

g = 9.81
FRACTION_MAX_DENOMINATOR = 10000
FRACTION_TOLERANCE = 1e-9


# ---------- SCREEN AND INPUT HELPERS ----------

def clear_screen():
    # Clears the TI-Nspire Python Shell. The fallback keeps the
    # program usable in a normal Python interpreter for testing.
    try:
        ti_system.disp_clr()
    except:
        print("\n" * 3)


def heading(title):
    clear_screen()
    print("=" * 32)
    print(title.center(32))
    print("=" * 32)


def ask(name, unit=""):
    while True:
        prompt = "  " + name
        if unit:
            prompt += " [" + unit + "]"
        prompt += ": "
        try:
            value = float(input(prompt))
            if math.isfinite(value):
                return value
        except:
            pass
        print("  Invalid number. Please try again.")


def ask_int(name):
    while True:
        value = ask(name)
        if value >= 1 and value == int(value):
            return int(value)
        print("  Enter a positive whole number.")


def pause():
    input("\n  Press Enter to return to the menu...")


# ---------- FRACTION DISPLAY ----------

def fraction_approx(value, max_denominator):
    """Return a reduced (numerator, denominator) approximation."""
    if not math.isfinite(value):
        return None

    sign = -1 if value < 0 else 1
    x = abs(value)

    if x == 0:
        return (0, 1)

    # Continued-fraction convergents.
    p0, q0 = 0, 1
    p1, q1 = 1, 0
    y = x

    for unused in range(32):
        a = int(y)
        p2 = a * p1 + p0
        q2 = a * q1 + q0

        if q2 > max_denominator:
            break

        p0, q0 = p1, q1
        p1, q1 = p2, q2

        remainder = y - a
        if remainder < 1e-15:
            break
