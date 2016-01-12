"""
An implementation of the boids project - refactored
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

numberOfBirds = 50
limitsPositionX = [-450.0, 50.0]
limitsPositionY = [300.0, 600.0]
limitsVelocityX = [0, 10.0]
limitsVelocityY = [-20.0, 20.0]

# position x,y for each boid
boids_x = [random.uniform(limitsPositionX[0], limitsPositionX[1]) for x in range(numberOfBirds)]
boids_y = [random.uniform(limitsPositionY[0], limitsPositionY[1]) for x in range(numberOfBirds)]
# velocity x,y for each boid
boid_x_velocities = [random.uniform(limitsVelocityX[0], limitsVelocityX[1]) for x in range(numberOfBirds)]
boid_y_velocities = [random.uniform(limitsVelocityY[0], limitsVelocityY[1]) for x in range(numberOfBirds)]
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


def update_boids(boids):
    collisionAlert = 100
    formationMaxLimit = 10000
    strengthToMiddle = 0.01
    strenghtToFormation = 0.125
    xs, ys, xvs, yvs = boids
    # Fly towards the middle
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            # for each boid i and each boid j
            xvs[i] = xvs[i] + (xs[j] - xs[i]) * strengthToMiddle / numberOfBirds
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            yvs[i] = yvs[i] + (ys[j] - ys[i]) * strengthToMiddle / numberOfBirds
    # Fly away from nearby boids
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            # is the distance (ssd) is lower than a critical value
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < collisionAlert:
                xvs[i] = xvs[i] + (xs[i] - xs[j])
                yvs[i] = yvs[i] + (ys[i] - ys[j])
    # Try to match speed with nearby boids
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            # match the speed only with the ones that are closer than 10000
            # 0.125 is the strength of the velocity
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < formationMaxLimit:
                xvs[i] = xvs[i] + (xvs[j] - xvs[i]) * strenghtToFormation / numberOfBirds
                yvs[i] = yvs[i] + (yvs[j] - yvs[i]) * strenghtToFormation / numberOfBirds
    # Move according to velocities
    for i in range(numberOfBirds):
        xs[i] = xs[i] + xvs[i]
        ys[i] = ys[i] + yvs[i]

xAxisLimits = [-500, 1500]
yAxisLimits = [-500, 1500]
figure = plt.figure()
axes = plt.axes(xlim=xAxisLimits, ylim=yAxisLimits)
scatter = axes.scatter(boids[0], boids[1])


def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0], boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
