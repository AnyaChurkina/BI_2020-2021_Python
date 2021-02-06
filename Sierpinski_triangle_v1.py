from random import randint
import matplotlib.pyplot as plt


def midpoint(p, q):
    return [0.5*(p[0] + q[0]), 0.5*(p[1] + q[1])]


n = 10000
point = [0, 0]

v1 = [0, 0]
v2 = [1, 0]
v3 = [0.5, 0.5 * 3 / 2]

for _ in range(n):
    val = randint(0, 2)
    if val == 0:
        point = midpoint(point, v1)
    if val == 1:
        point = midpoint(point, v2)
    if val == 2:
        point = midpoint(point, v3)
    plt.plot(point[0], point[1], '^', markersize=3)

plt.title("Sierpinski triangle")
plt.title("Sierpinski triangle")
plt.savefig("Sierpinski_triangle_v1.png")
plt.show()
