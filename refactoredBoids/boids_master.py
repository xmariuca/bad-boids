'''
Main class for controlling the boids
'''
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

class BoidsMaster:
    def __init__(self, position_limits = np.array([[-450.0, 50.0], [300.0, 600.0]]), velocity_limits = np.array([[0, 10.0], [-20.0, 20.0]]), boids_number = 50, collision_alert = 100, formation_limit = 10000, strength2middle = 0.01, strength2formation = 0.125):
        self.position_limits = position_limits
        self.velocity_limits = velocity_limits
        self.boids_number = boids_number
        self.collision_alert = collision_alert
        self.formation_limit = formation_limit
        self.strength2middle = strength2middle
        self.strength2formation = strength2formation
        self.positions = self.__new_boids(self.position_limits)
        self.velocities = self.__new_boids(self.velocity_limits)

    def set_boids(self, new_positions, new_velocities):
        self.positions = new_positions
        self.velocities = new_velocities

    def __new_boids(self, limits):
        lower_limits = limits[:,0]
        upper_limits = limits[:,1]
        width = upper_limits - lower_limits
        return (lower_limits[:,np.newaxis] + np.random.rand(2,self.boids_number) * width[:,np.newaxis])

    def fly_towards_center(self):
        center = np.mean(self.positions,1)
        direction_to_center = self.positions - center[:, np.newaxis]
        self.velocities = self.velocities - direction_to_center * self.strength2middle

    def fly_away_from_neighbours(self):
        positionsX = self.positions[0,:]
        positionsY = self.positions[1,:]
        velocitiesX = self.velocities[0,:]
        velocitiesY = self.velocities[1,:]

        for i in range(self.boids_number):
            for j in range(self.boids_number):
                # is the distance (ssd) is lower than a critical value
                if (positionsX[j] - positionsX[i]) ** 2 + (positionsY[j] - positionsY[i]) ** 2 < self.collision_alert:
                    velocitiesX[i] = velocitiesX[i] + (positionsX[i] - positionsX[j])
                    velocitiesY[i] = velocitiesY[i] + (positionsY[i] - positionsY[j])
        self.positions[0,:] = positionsX
        self.positions[1,:] = positionsY
        self.velocities[0,:] = velocitiesX
        self.velocities[1,:] = velocitiesY

    def match_speed_w_neighbours(self):
        positionsX = self.positions[0,:]
        positionsY = self.positions[1,:]
        velocitiesX = self.velocities[0,:]
        velocitiesY = self.velocities[1,:]

        for i in range(self.boids_number):
            for j in range(self.boids_number):
                # match the speed only with the ones that are closer than 10000
                # 0.125 is the strength of the velocity
                if (positionsX[j] - positionsX[i]) ** 2 + (positionsY[j] - positionsY[i]) ** 2 < self.formation_limit:
                    velocitiesX[i] = velocitiesX[i] + (velocitiesX[j] - velocitiesX[i]) * self.strength2formation / self.boids_number
                    velocitiesY[i] = velocitiesY[i] + (velocitiesY[j] - velocitiesY[i]) * self.strength2formation / self.boids_number
        self.positions[0,:] = positionsX
        self.positions[1,:] = positionsY
        self.velocities[0,:] = velocitiesX
        self.velocities[1,:] = velocitiesY

    def update_positions(self):
        self.positions += self.velocities

    def update_boids(self):
        self.fly_towards_center()
        self.fly_away_from_neighbours()
        self.match_speed_w_neighbours()
        self.update_positions()
