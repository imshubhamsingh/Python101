import matplotlib.pyplot as plt
import numpy as np

# x1 = [1, 3, 5, 7, 9]
# y1 = [2, 4, 6, 8, 10]
#
# x2 = [2, 4, 6, 8, 10]
# y2 = [2, 4, 6, 8, 10]
#
# plt.bar(x1, y1, label='bars 1', color='r')
# plt.bar(x2, y2, label='bars 2', color='c')
#

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 99, 102, 110, 120, 121, 130, 111, 115, 112, 80, 75, 65, 54, 44,
                   43, 42, 48]

# id = [x for x in range(len(population_ages))]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, label='1')
plt.hist(population_ages, bins, histtype='bar', rwidth=0.1, label='2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.legend()
plt.show()
