import random

countSum = 0   # sum of numbers necessary to get past 1.0
for i in range (1, 1001):
    sum = 0         # running sum
    
    while (sum < 1.0):
        countSum += 1
        sum += random.random()

    if (i % 100 == 0):
        print(countSum/i)