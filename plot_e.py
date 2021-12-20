import matplotlib.pyplot as plt
import numpy as np
import generate_e
import math

degree = 10000
approximations = generate_e.generate_e(degree)

xpoints = np.array(range(1, degree + 1))
ypoints = np.array(approximations)

plt.plot(xpoints, ypoints, label="Approximations")

plt.axhline(math.e, color='green', label="constant e", linestyle='dashed')
plt.xlim(1, degree)

plt.legend()
plt.show()