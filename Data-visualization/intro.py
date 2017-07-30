import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0, 100, 0.01)
y1 = np.sin(x1)

x2 = np.arange(0, 100, 0.01)
y2 = np.cos(x2)

plt.plot(x1, y1, label='sine fn.')
plt.plot(x2, y2, label='cosine fn.')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometry functions')
plt.legend()

plt.show()
