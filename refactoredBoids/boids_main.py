from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from boids_master import BoidsMaster

position_limits = np.array([[-450.0, 50.0], [300.0, 600.0]])
velocities_limits = np.array([[0, 10.0], [-20.0, 20.0]])
boids_number = 50;
master_of_boids = BoidsMaster(position_limits,velocities_limits, boids_number)
# master_of_boids = BoidsMaster()


xAxisLimits = np.array([-500, 1500])
yAxisLimits = np.array([-500, 1500])
figure = plt.figure()
axes = plt.axes(xlim=xAxisLimits, ylim=yAxisLimits)
scatter = axes.scatter(master_of_boids.positions[0,:], master_of_boids.positions[1,:])

def animate(frame):
    master_of_boids.update_boids()
    scatter.set_offsets(zip(master_of_boids.positions[0,:], master_of_boids.positions[1,:]))


anim = animation.FuncAnimation(figure, animate,frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
