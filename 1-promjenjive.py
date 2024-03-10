# # # promjenjljive ili varijable, mjesta u memoriji koje mozemo da cuvamo podatke

# # ime = 'mare'   #ovo je string i zato je pod navodnicima
# # starost = '41'   #ovo je integer, moras sve staviti pod navodnike zbog pocetnog stringa ili nece raditi
# # visina = '1.69'  #ovo je float zbog tocke
# # print (ime + ' je visoka ' + visina + ' cm' +  ' i ima ' +  starost +  ' godinu') 

#ili mozes ovako

# ime = 'mare'
# starost = 41
# visina = 1.69
# print(ime + ' je visoka ' + str(visina) + ' i ima godina ' + str(starost))

# ime = input ('unesi ime: ')
# godine = input('unesi godine: ')  
# visina = input('unesi visinu: ')
# print(ime)
# print(godine)
# print(visina)

num1 = int(input('unesi prvi broj: '))
num2 = int(input('unesi drugi broj: '))
rezultat = num1 + num2
print('Rezultat zbrajanja je ', rezultat)