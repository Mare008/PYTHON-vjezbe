#Ova je funkcija
def fun(x):
    rezultat = 4*x**3+0.5*x-3
    return rezultat

#Definicija koordinatne mreže
N = 101 #Broj točaka mreže
x0 = 0.0 #Početna točka mreže
xn = 1.0 #Konačna točka mreže
h = (xn-x0)/(N-1) #Razmak između točaka

for i in range(0,N+1,1):
   x = i*h+x0
   print(x,fun(x))

