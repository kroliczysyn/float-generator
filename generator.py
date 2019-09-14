import random
import csv

input_list = []
output_list = []
iterations = 1000000
with open('input.csv', 'w', newline='') as csvfile:
    for i in range(iterations):
        a = random.uniform(0, 1000)
        b = random.uniform(0, 1000)
        c = random.uniform(-1, 1)
        d = random.uniform(-1, 1)
        x = a - c
        y = b - d
        data_output = (x, y)
        output_list.append(data_output)
        data = (a, b)
        input_list.append(data)
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(data)

with open('output.csv', 'w', newline='') as csvfile:
    for k in range(iterations):
        data_final_output = (output_list[k][0], output_list[k][1])
        outputwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        outputwriter.writerow(data_final_output)