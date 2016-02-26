from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from boids_master import BoidsMaster


def main_animate_boids(number_boids = 50,
                         collision_alert = 100,
                         formation_limit = 10000,
                         strength2middle = 0.01,
                         strength2formation = 0.125):
    '''
    This function initializes a BoidsMaster object that controlls the behaviour of the boids. The input parameters influence the simulation.

    :param number_boids: The number of boids to include in the simulation
    :type number_boids: int
    :param collision_alert: Sets which boids are considered neighbours in order to avoid collisions with them
    :type collision_alert: int
    :param formation_limit: Sets which boids are supposed to fly in a formation with matching speed
    :type formation_limit: int
    :param strength2middle: Sets the strength with which the boids fly towards the middle of the flock
    :type strength2middle: float
    :param strength2formation: Sets the strength of the flying in the same formation
    :type strength2formation: float

    :returns: An animation of the animated boid simulation and an .mp4 video with the recording.
    '''
    if not isinstance(number_boids, int):
        raise ValueError("The number of boids: " +
                         str(number_boids) + " is not an integer")
    if not isinstance(collision_alert, int):
        raise ValueError("The collision alert: " +
                         str(collision_alert) + " is not an integer")
    if not isinstance(formation_limit, int):
        raise ValueError("The formation limit: " +
                         str(formation_limit) + " is not an integer")
    if not isinstance(strength2middle, float):
        raise ValueError("The strength to middle: " +
                         str(strength2middle) + " is not an integer")
    if not isinstance(strength2formation, float):
        raise ValueError("The strength to formation: " +
                         str(strength2formation) + " is not an integer")

    if number_boids <= 0:
        raise ValueError("The number of boids: " +
                         str(number_boids) + " is non-positive")

    if collision_alert <= 0:
        raise ValueError("The collision alert: " +
                         str(collision_alert) + " is non-positive")

    if formation_limit <= 0:
        raise ValueError("The formation alert: " +
                         str(formation_limit) + " is non-positive")

    if strength2middle <= 0:
        raise ValueError("The strength to middle: " +
                         str(strength2middle) + " is non-positive")

    if strength2formation <= 0:
        raise ValueError("The strength to formation: " +
                         str(strength2formation) + " is non-positive")


    position_limits=np.array([[-450.0, 50.0], [300.0, 600.0]])
    velocity_limits=np.array([[0, 10.0], [-20.0, 20.0]])

    master_of_boids = BoidsMaster(position_limits,
                                  velocity_limits,
                                  number_boids,
                                  collision_alert,
                                  formation_limit,
                                  strength2middle,
                                  strength2formation)
    master_of_boids.start_animation()


if __name__ == "__main__":
    main_animate_boids()
