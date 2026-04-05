ZAHL_1: float = 8.0
ZAHL_2: float = 4.0
ABSTAND: float = 0.1
total: float = 0


def numerikrechner():
    global ZAHL_2
    global total
    while ZAHL_2 < ZAHL_1:
        total += 4 * (ZAHL_2**2) * ABSTAND
        ZAHL_2 += ABSTAND


numerikrechner()
print(f"Das Integral ist ungefähr {total} ")
