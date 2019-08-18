import random
import csv

input_list = []
output_list = []
iterations = 1000000

for i in range(iterations):
    a = random.uniform(0, 1000)
    b = random.uniform(0, 1000)
    input_list.append(a)
    input_list.append(b)
    c = random.uniform(-3, 3)
    d = random.uniform(-3, 3)
    x = a - c
    y = b - d
    output_list.append(x)
    output_list.append(y)

with open('input.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(input_list)

print("Input list: ")

with open('input.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        for i in range(iterations):
            print(row[i])

with open('output.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(output_list)

print("Output list: ")

with open('output.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        for i in range(iterations):
            print(row[i])
