# To calculate the mean absolute deviation of given data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sec_a = np.array([75 , 65, 73, 68 , 72, 76])
sec_b = np.array([90, 47, 43, 96, 93, 51])
mean_sec_a = sec_a.mean()
mean_sec_b = sec_b.mean()

# calucation of mean absoule deviation

mad_sec_a = np.sum(np.abs(sec_a - mean_sec_a))/len(sec_a)
mad_sec_b = np.sum(np.abs(sec_b - mean_sec_b))/len(sec_b)
no = [i for i in range(0,6)]
print(f"MAD of Sec_a and Sec_b is {mad_sec_a} and {mad_sec_b}")

plt.scatter(sec_a, no, label = "sec_a")
plt.scatter(sec_b, no, color = "red", marker = "*", label = "sec_b")
plt.plot ([mean_sec_a for i in range(0,6)], [i for i in range(0,6)], color = "yellow", label = "Mean")
plt.legend()
plt.show()