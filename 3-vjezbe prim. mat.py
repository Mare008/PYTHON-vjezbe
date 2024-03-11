napon = []
struja = []

with open('measurments.txt', 'r') as file:
    for line in file:
        napon_str, struja_str = line.split()
        napon.append(float(napon_str))
        struja.append(float(struja_str))

print("Napon:", napon)
print("Struja:", struja)

# #Kreirajmo datoteku measurements.txt s mjerenjima napona i struje u
# nekom od uređivača teksta: i save u file od pythona gdje su ti python vjezbe
#jer inace nece citati file koji pozivas
# 0.5 10
# 1.0 20
# 1.5 30
# 2.0 40
# 2.5 50
