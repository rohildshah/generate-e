import random

sum = 0     # running sum
count = 0   # number of numbers summed so far
while (sum < 1.0):
    count += 1
    sum += random.random()

print(count)