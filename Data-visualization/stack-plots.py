import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [6, 8, 11, 7, 9]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], label='sleeping', color='m', linewidth=8)
plt.plot([], [], label='eating', color='c', linewidth=8)
plt.plot([], [], label='working', color='r', linewidth=8)
plt.plot([], [], label='playing', color='k', linewidth=8)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

plt.xlabel('days')
plt.ylabel('activities')
plt.legend()
plt.show()
