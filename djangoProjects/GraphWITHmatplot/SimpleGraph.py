import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [5, 8, 10]
y = [12, 16, 6]

x1 = [6,9,11]
y1 = [6,15,7]


plt.plot(x, y, 'g', label="line one", linewidth=5)
plt.plot(x1, y1, 'c', label="line one", linewidth=5)

plt.title("Info of graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.legend()
plt.grid(True, color = 'k')
plt.show()
