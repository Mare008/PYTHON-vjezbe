# Definicija funkcije za numeričku aproksimaciju druge derivacije kroz središnju razliku
def numeric_second_derivative(fun, x, h):
    return (fun(x + h) - 2 * fun(x) + fun(x - h)) / (h**2)

# Definicija funkcije
def fun(x):
    return (x**2 + 7)**2

# Definicija koordinatne mreže
N = 101  # Broj točaka mreže
x0 = 0.0  # Početna točka mreže
xn = 1.0  # Konačna točka mreže
h = (xn - x0) / (N - 1)  # Razmak između točaka

# Računanje numeričke aproksimacije druge derivacije kroz središnju razliku
print("x\tNumericka druga derivacija")
for i in range(1, N, 1):
    x = i * h + x0
    numeric_second_deriv = numeric_second_derivative(fun, x, h)
    print(f"{x}\t{numeric_second_deriv}")