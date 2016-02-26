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

def test_main_collision_alert_int():
    '''
    Test - the collision alert has to be an integer
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    '4',
                                    formation_limit,
                                    strength2middle,
                                    strength2formation)

def test_main_collision_alert_positive():
    '''
    Test - the collision alert has to be positive
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    -100,
                                    formation_limit,
                                    strength2middle,
                                    strength2formation)

def test_main_formation_limit_int():
    '''
    Test - the formation limit has to be an integer
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    collision_alert,
                                    '3',
                                    strength2middle,
                                    strength2formation)

def test_main_formation_limit_positive():
    '''
    Test - the formation limit has to be positive
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    collision_alert,
                                    -2,
                                    strength2middle,
                                    strength2formation)

def test_main_strength2middle_int():
    '''
    Test - the strength to middle has to be a float
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    collision_alert,
                                    formation_limit,
                                    '0.1',
                                    strength2formation)

def test_main_strength2middle_positive():
    '''
    Test - the strength to middle has to be positive
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    collision_alert,
                                    formation_limit,
                                    -0.9,
                                    strength2formation)

def test_main_strength2formation_int():
    '''
    Test - the strength to formation has to be a float
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    collision_alert,
                                    formation_limit,
                                    strength2middle,
                                    '0.9')

def test_main_strength2formation_positive():
    '''
    Test - the strength to formation has to be positive
    '''
    with assert_raises(ValueError):
        assert main_animate_boids(boids_number,
                                    collision_alert,
                                    formation_limit,
                                    strength2middle,
                                    -1.0)
