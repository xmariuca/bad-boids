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
        self.velocities -= direction_to_center * self.strength2middle

    def fly_away_from_neighbours(self):
        distance_mat = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_distance_mat = distance_mat * distance_mat
        square_distances_sum = np.sum(squared_distance_mat, 0)
        far_away = square_distances_sum > self.collision_alert

        neighbours_if_close = np.copy(distance_mat)
        neighbours_if_close[0,:,:][far_away] = 0
        neighbours_if_close[1,:,:][far_away] = 0
        self.velocities += np.sum(neighbours_if_close,1)

    def match_speed_w_neighbours(self):
        distance_mat = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_distance_mat = distance_mat * distance_mat
        square_distances_sum = np.sum(squared_distance_mat, 0)

        velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        very_far = square_distances_sum > self.formation_limit
        neighbours_if_close = np.copy(velocity_differences)
        neighbours_if_close[0,:,:][very_far] = 0
        neighbours_if_close[1,:,:][very_far] = 0
        self.velocities -= np.mean(neighbours_if_close, 1) * self.strength2formation

    def update_positions(self):
        self.positions += self.velocities

    def update_boids(self):
        self.fly_towards_center()
        self.fly_away_from_neighbours()
        self.match_speed_w_neighbours()
        self.update_positions()
