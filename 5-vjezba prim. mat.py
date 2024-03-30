napon = [0.5, 1.0, 1.5, 2.0, 2.5]
struja = [10, 20, 30, 40, 50]
filename = 'izlaz.txt'

with open(filename, 'w') as file:
     for i in range(len(napon)):
         file.write(f"{napon[i]} {struja[i]}\n")
print(f"Podaci su uspjesno zapisani u datoteku {filename}.")
