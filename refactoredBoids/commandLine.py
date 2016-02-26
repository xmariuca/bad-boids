#!/usr/bin/env python
from argparse import ArgumentParser
from boids_master import BoidsMaster
from boids_main import main_animate_boids

def parseArgs():
    '''
    Entry point from the command line.

    :Example:

    >>> simulate_boids --number_boids 50 --collision_alert 100 --formation_limit 10000 --strength_to_middle 0.01 --strength_to_formation 0.125
    '''
    prs = ArgumentParser(description =
                         "Boids Simulator - generates a flock of birds " +
                         "and simulates its flying behaviour based on the" +
                         "input parameters.")

    prs.add_argument('--number_boids',
                     help='Number of boids, default = 50',
                     dest='number_boids', default = 50, type = int)
    prs.add_argument('--collision_alert',
                     help = 'Collision alert, default = 100',
                     dest='collision_alert', default = 100, type = int)
    prs.add_argument('--formation_limit',
                     help='Formation limit, default = 10000',
                     default = 10000, type = int)
    prs.add_argument('--strength_to_middle',
                     help = 'Strength to flock center, default = 0.01',
                     default = 0.01, type = float)
    prs.add_argument('--strength_to_formation',
                  help = 'Strength to formation, default = 0.0125',
                  default = 0.0125, type = float)
    arguments = prs.parse_args()

    main_animate_boids(arguments.number_boids,
                       arguments.collision_alert,
                       arguments.formation_limit,
                       arguments.strength_to_middle,
                       arguments.strength_to_formation)

if __name__=='__main__':
    parseArgs()
