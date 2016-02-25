"""
An implementation of the boids project - refactored
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

numberOfBirds = 50
limitsPositionX = np.array([-450.0, 50.0])
limitsPositionY = np.array([300.0, 600.0])
limitsVelocityX = np.array([0, 10.0])
limitsVelocityY = np.array([-20.0, 20.0])

# create function to generate random numbers for position & velocity
# def new_boids(count, lower_limits, upper_limits):
#     width = upper_limits - lower_limits
#     return (lower_limits(:,np.newaxis) + np.random.rand(2,count) * width[]:,np.newaxis])


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
    positionX, positionY, velocityX, velocityY = boids
    # Fly towards the middle
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            # for each boid i and each boid j
            velocityX[i] = velocityX[i] + (positionX[j] - positionX[i]) * strengthToMiddle / numberOfBirds
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            velocityY[i] = velocityY[i] + (positionY[j] - positionY[i]) * strengthToMiddle / numberOfBirds
    # Fly away from nearby boids
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            # is the distance (ssd) is lower than a critical value
            if (positionX[j] - positionX[i]) ** 2 + (positionY[j] - positionY[i]) ** 2 < collisionAlert:
                velocityX[i] = velocityX[i] + (positionX[i] - positionX[j])
                velocityY[i] = velocityY[i] + (positionY[i] - positionY[j])
    # Try to match speed with nearby boids
    for i in range(numberOfBirds):
        for j in range(numberOfBirds):
            # match the speed only with the ones that are closer than 10000
            # 0.125 is the strength of the velocity
            if (positionX[j] - positionX[i]) ** 2 + (positionY[j] - positionY[i]) ** 2 < formationMaxLimit:
                velocityX[i] = velocityX[i] + (velocityX[j] - velocityX[i]) * strenghtToFormation / numberOfBirds
                velocityY[i] = velocityY[i] + (velocityY[j] - velocityY[i]) * strenghtToFormation / numberOfBirds
    # Move according to velocities
    for i in range(numberOfBirds):
        positionX[i] = positionX[i] + velocityX[i]
        positionY[i] = positionY[i] + velocityY[i]

xAxisLimits = np.array([-500, 1500])
yAxisLimits = np.array([-500, 1500])
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
