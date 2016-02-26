from nose.tools import assert_raises
from refactoredBoids.boids_main import *

boids_number = 50
collision_alert = 100
formation_limit = 10000
strength2middle = 0.01
strength2formation = 0.125

def test_main_number_boids_int():
    '''
    Test - the number of boids has to be an integer
    '''
    with assert_raises(ValueError):
        assert main_animate_boids('50',
                                    collision_alert,
                                    formation_limit,
                                    strength2middle,
                                    strength2formation)

def test_main_number_boids_positive():
    '''
    Test - the number of boids has to be positive
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(-3,
                                    collision_alert,
                                    formation_limit,
                                    strength2middle,
                                    strength2formation)
