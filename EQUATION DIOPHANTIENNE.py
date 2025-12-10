# PGCD avec Euclide
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

# Euclide étendu
def euclide_etendu(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0  # d, x0, y0

# Programme principal
a = int(input("Entrer a : "))
b = int(input("Entrer b : "))
c = int(input("Entrer c : "))

A, B = a, b

d, x0, y0 = euclide_etendu(a, b)
print(f"PGCD({A},{B}) = {d}")
print(f"Coefficients de Bézout : x0={x0}, y0={y0}")

if c % d != 0:
    print("Pas de solution entière")
else:
    print("Il existe des solutions entières")

    # Solution particulière
    k = c // d
    xp = x0 * k
    yp = y0 * k
    print(f"Solution particulière : xp={xp}, yp={yp}")

    # Solution générale
    alpha = B // d
    beta = -A // d
    print(f"Forme générale : x = {xp} + {alpha}*k, y = {yp} + {beta}*k, k ∈ Z")

    # Quelques exemples
    for k_val in range(-2, 3):
        xk = xp + alpha * k_val
        yk = yp + beta * k_val
        print(f"k={k_val} -> x={xk}, y={yk}")
