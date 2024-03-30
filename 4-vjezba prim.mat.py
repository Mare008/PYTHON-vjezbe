napon = []
struja = []
try:
    with open('proba.txt', 'r') as file:
        for line in file:
            napon_str, struja_str = line.split()
            napon.append(float(napon_str))
            struja.append(float(struja_str))

except FileNotFoundError:
    print("Datoteka ne postoji!")

