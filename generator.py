import random
import csv

def get_value():
    return float(value)


lista_wej = []
lista_wyj = []

for i in range(5):
    a = random.uniform(0, 1000)
    b = random.uniform(0, 1000)
    lista_wej.append(a)
    lista_wej.append(b)
    c = random.uniform(-3, 3)
    d = random.uniform(-3, 3)
    x = a - c
    y = b - d
    lista_wyj.append(x)
    lista_wyj.append(y)

print("Teraz lista idzieeeeee: " + str(lista_wej))
print("Teraz druga lista idzieeeeee: " + str(lista_wyj))

with open('input.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(lista_wej)

print("teraz pójdą dane wejściowe")

with open('input.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

with open('output.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(lista_wyj)

print("teraz pójdą dane wyjściowe")

with open('output.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

