import random

def generate_e(degree):
    countSum = 0        # sum of numbers necessary to get past 1.0
    approximations = [] # list of approximations
    for i in range (1, degree + 1):
        sum = 0         # running sum
        
        while (sum < 1.0):
            countSum += 1
            sum += random.random()

        approximations.append(countSum/i)

    return approximations