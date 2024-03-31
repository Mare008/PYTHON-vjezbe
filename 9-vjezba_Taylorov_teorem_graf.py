import numpy as np
import matplotlib.pyplot as plt

# Definiraj funkcije
def fun(x):
    return 4*x**3 + 0.5*x - 3

def fun1(x):
    return 12*x**2 + 0.5

# Definiraj derivaciju koristeći 5-točkovnu formulu
def derivacija_5_tocaka(x, h):
    N = len(x)
    deriv = np.zeros(N)

    for i in range(N):
        if i == 0:
            deriv[i] = (-25.0*fun(x[i]) + 48.0*fun(x[i]+h) - 36.0*fun(x[i]+2*h) + 16.0*fun(x[i]+3*h) -3.0*fun(x[i]+4*h))/(12*h)
        elif i == 1:
            deriv[i] = (-3.0*fun(x[i]-h) - 10.0*fun(x[i]) + 18.0*fun(x[i]+h) -6.0*fun(x[i]+2*h) +fun(x[i]+3*h))/(12*h)
        elif i == N-1:
            deriv[i] = (3.0*fun(x[i]+h) + 10.0*fun(x[i]) - 18.0*fun(x[i]-h) +6.0*fun(x[i]-2*h) -fun(x[i]-3*h))/(12*h)
        else:
            deriv[i] = (fun(x[i]-2*h) -8.0*fun(x[i]-h) + 8.0*fun(x[i]+h) - fun(x[i]+2*h))/(12*h)
    
    return deriv
# Definiraj raspon i korak za x-vrijednosti
x_vrijednosti = np.linspace(0, 1, 1000)  # Prilagodi broj točaka za glatkije krivulje
h = (x_vrijednosti[-1] - x_vrijednosti[0]) / (len(x_vrijednosti) - 1)

# Izračunaj vrijednosti funkcija
fun_vrijednosti = fun(x_vrijednosti)
fun1_vrijednosti = fun1(x_vrijednosti)
derivacija_5_tocaka_vrijednosti = derivacija_5_tocaka(x_vrijednosti, h)

# Prikazi fun1 i njezinu prvu derivaciju koristeći formulu s 5 točaka
plt.figure(figsize=(10, 6))

plt.plot(x_vrijednosti, fun1_vrijednosti, label='fun1(x)', color='green')
plt.plot(x_vrijednosti, derivacija_5_tocaka_vrijednosti, label='Približna derivacija', linestyle='--', color='orange')

plt.title('Grafovi Funkcije i Približne Derivacije')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()