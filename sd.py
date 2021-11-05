import math
import csv
with open("data.csv", newline = '') as f :
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + int(x)
    mean = total/n
    print(mean)
    return mean

squared_list = []
for x in data:
    a = int(x) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for x in squared_list:
    sum = sum + x
result = sum/(len(data) - 1)
sd = math.sqrt(result)
print(result)
print(sd)