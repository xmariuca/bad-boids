import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class BoidsMaster(object):
    '''
    Main class - the BoidMaster controlls the behaviour of the boids.
    '''
    def __init__(self,
                 position_limits=np.array([[-450.0, 50.0], [300.0, 600.0]]),
                 velocity_limits=np.array([[0, 10.0], [-20.0, 20.0]]),
                 boids_number=50,
                 collision_alert=100,
                 formation_limit=10000,
                 strength2middle=0.01,
                 strength2formation=0.125):
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
        '''
        .. method:: Sets given positions and velocities to a BoidsMaster object. This is mostly used for testing purposes.
        '''
        self.positions = new_positions
        self.velocities = new_velocities

    def __new_boids(self, limits):
        '''
        .. method:: Creates a list of random values inside a given interval. Used for generating random positions and velocities for the flock.
        '''
        lower_limits = limits[:, 0]
        upper_limits = limits[:, 1]
        width = upper_limits - lower_limits
        return (lower_limits[:, np.newaxis] +
                np.random.rand(2, self.boids_number) *
                width[:, np.newaxis])

    def fly_towards_center(self):
        '''
        .. method:: Makes the boids fly towards the center of the flock. Modify how fast they move by setting the strength2middle[float] member to different values.
        '''
        center = np.mean(self.positions, 1)
        # get the vector that shows the direction to the center of the flock
        direction_to_center = self.positions - center[:, np.newaxis]
        # make the boids move in the middle direction
        self.velocities -= direction_to_center * self.strength2middle

    def fly_away_from_neighbours(self):
        '''
        .. method:: Avoids collision with neighbouring boids. Modify which boids are considered far away by setting the member collision_alert[int].
        '''
        # compute the squared distances between all the boids
        distance_mat = self.positions[:, np.newaxis, :] - \
            self.positions[:, :, np.newaxis]
        squared_distance_mat = distance_mat * distance_mat
        square_distances_sum = np.sum(squared_distance_mat, 0)
        far_away = square_distances_sum > self.collision_alert
        # exclude the boids that are too far away
        neighbours_if_close = np.copy(distance_mat)
        neighbours_if_close[0, :, :][far_away] = 0
        neighbours_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(neighbours_if_close, 1)

    def match_speed_w_neighbours(self):
        '''
        .. method:: Match speed with the neighbouring boids. Modify which boids are considered neighbours through the member formation_limit[int]. Modify the flying strength through strength2formation[float].
        '''
        distance_mat = self.positions[:, np.newaxis, :] - \
            self.positions[:, :, np.newaxis]
        squared_distance_mat = distance_mat * distance_mat
        square_distances_sum = np.sum(squared_distance_mat, 0)

        velocity_differences = self.velocities[:, np.newaxis, :] - \
            self.velocities[:, :, np.newaxis]
        very_far = square_distances_sum > self.formation_limit
        neighbours_if_close = np.copy(velocity_differences)
        neighbours_if_close[0, :, :][very_far] = 0
        neighbours_if_close[1, :, :][very_far] = 0
        self.velocities -= np.mean(neighbours_if_close, 1) * \
            self.strength2formation

    def update_positions(self):
        '''
        .. method:: Updates the positions of the boids according to their velocities.
        '''
        self.positions += self.velocities

    def update_boids(self):
        '''
        .. method:: Updates the positions of the boids after all of their behaviours are called: fly_towards_center(), fly_away_from_neighbours() and match_speed_w_neighbours().
        '''
        self.fly_towards_center()
        self.fly_away_from_neighbours()
        self.match_speed_w_neighbours()
        self.update_positions()

    def __animate_iteration(self, frame):
        '''
        .. method:: Private method that updates the scatter plot to show the new positions of the boids after update_boids() is called.
        '''
        self.update_boids()
        self.scatter.set_offsets(zip(self.positions[0, :],
                                     self.positions[1, :]))

    def start_animation(self):
        '''
        .. method:: Start the animation of the boids.
        '''
        xAxisLimits = np.array([-500, 1500])
        yAxisLimits = np.array([-500, 1500])
        figure = plt.figure()
        axes = plt.axes(xlim=xAxisLimits, ylim=yAxisLimits)
        self.scatter = axes.scatter(self.positions[0, :],
                                    self.positions[1, :])
        anim = animation.FuncAnimation(figure, self.__animate_iteration, frames=50, interval=50)
        plt.show()
