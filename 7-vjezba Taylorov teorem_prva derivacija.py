#Ova je funkcija
def fun(x):
    rezultat = 4*x**3+0.5*x-3
    return rezultat

#Ovo je prva derivacija funkcije
def fun1(x):
    rezultat = 12*x**2 + 0.5
    return rezultat

#Definicija koordinatne mreže
N = 101 #Broj točaka mreže
x0 = 0.0 #Početna točka mreže
xn = 1.0 #Konačna točka mreže
h = (xn-x0)/(N-1) #Razmak između točaka


#Središnja razlika - prva derivacija
for i in range(1,N,1):
   x = i*h+x0
   prva_der = (fun(x+h)-fun(x-h))/(2.0*h)
   print(x,prva_der,fun1(x))

