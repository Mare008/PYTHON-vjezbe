# Definicija funkcije
def fun(x):
    return (x**2 + 7)**2

# Definicija funkcije za numeričku aproksimaciju prve derivacije kroz središnju razliku
def numeric_derivative(fun, x, h):
    return (fun(x + h) - fun(x - h)) / (2.0 * h)

# Definicija koordinatne mreže
N = 101  # Broj točaka mreže
x0 = 0.0  # Početna točka mreže
xn = 1.0  # Konačna točka mreže
h = (xn - x0) / (N - 1)  # Razmak između točaka

# Računanje numeričke aproksimacije prve derivacije kroz središnju razliku
print("x\tNumericka derivacija")
for i in range(1, N, 1):
    x = i * h + x0
    numeric_deriv = numeric_derivative(fun, x, h)
    print(f"{x}\t{numeric_deriv}")