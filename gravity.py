import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
points, = ax.plot([], [])


def init():
    points.set_data([], [])
    return points,

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    z = np.cos(2 * np.pi * (x - 0.01 * i))
    points.set_data(x, y)
    return points

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()

