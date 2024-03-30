#Ova je funkcija
def fun(x):
    rezultat = 4*x**3+0.5*x-3
    return rezultat

#Ovo je druga derivacija funkcije
def fun2(x):
    rezultat = 24*x
    return rezultat

#Definicija koordinatne mreže
N = 101 #Broj točaka mreže
x0 = 0.0 #Početna točka mreže
xn = 1.0 #Konačna točka mreže
h = (xn-x0)/(N-1) #Razmak između točaka



#Središnja razlika - druga derivacija
for i in range(1,N,1):
    x = i*h+x0
    druga_der = (fun(x+h)-2*fun(x)+fun(x-h))/(h*h)
    print(x,druga_der,fun2(x))