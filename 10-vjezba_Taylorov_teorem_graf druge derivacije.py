import numpy as np
import matplotlib.pyplot as plt

# Definiraj funkcije
def fun(x):
    return 4*x**3 + 0.5*x - 3

def fun1(x):
    return 12*x**2 + 0.5
def fun2(x):
    rezultat = 24*x
    return rezultat

# Definiraj derivaciju koristeci 5-tockovnu formulu
def derivacija_5_tocaka(x, h):
    N = len(x)
    deriv = np.zeros(N)

    for i in range(N):

        
        if i == 0:#necentralni 1. izraz
            deriv[i] = (35*fun(x[i]) - 104*fun(x[i]+h) + 114*fun(x[i]+2*h) -56*fun(x[i]+3*h) +11*fun(x[i]+4*h))/12/h/h
        elif i == 1:#necentralni 2. izraz
            deriv[i] = (11*fun(x[i]-h) - 20*fun(x[i]) + 6*fun(x[i]+h) +4*fun(x[i]+2*h) -fun(x[i]+3*h))/12/h/h
        elif i == N-1:#necentralni 4. izraz
            deriv[i] = (11*fun(x[i]+h) - 20*fun(x[i]) + 6*fun(x[i]-h) + 4*fun(x[i]-2*h) -fun(x[i]-3*h))/12/h/h
        elif i == N: #necentralni 5. izraz
            deriv[i] = (35*fun(x[i]) -104 *fun(x[i]-h) + 114*fun(x[i]-2*h) - 56*fun(x[i]-3*h) +11*fun(x[i]-4*h))/12/h/h
        else: #centralni 3. izraz
            deriv[i] = (-fun(x[i]-2*h) + 16*fun(x[i]-h) - 30*fun(x[i]) +16*fun(x[i]+h)-fun(x[i]+2*h))/12/h/h


    return deriv

# Definiraj raspon i korak za x-vrijednosti
x_vrijednosti = np.linspace(0, 1, 1000)  # Prilagodi broj tocaka za glatkije krivulje
h = (x_vrijednosti[-1] - x_vrijednosti[0]) / (len(x_vrijednosti) - 1)

# Izracunaj vrijednosti funkcija
fun_vrijednosti = fun(x_vrijednosti)
fun1_vrijednosti = fun2(x_vrijednosti)
derivacija_5_tocaka_vrijednosti = derivacija_5_tocaka(x_vrijednosti, h)

# Prikazi fun1 i njezinu prvu derivaciju koristeci formulu s 5 tocaka
plt.figure(figsize=(10, 6))

plt.plot(x_vrijednosti, fun1_vrijednosti, label='fun2(x)', color='green')
plt.plot(x_vrijednosti, derivacija_5_tocaka_vrijednosti, label='Približna derivacija', linestyle='--', color='orange')

plt.title('Grafovi Funkcije i Približne Derivacije')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()