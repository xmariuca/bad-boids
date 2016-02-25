from refactoredBoids.boids_master import BoidsMaster
from nose.tools import assert_almost_equal
import numpy as np
import os
import yaml

def test_refactored_class_boids_regression():
    '''
    Regression test - Tests that the class written for the boids works with the initial fixtures
    '''
    regression_data = yaml.load(open(
    os.path.join(os.path.dirname(__file__), 'fixtures/fixture.yml')))
    boid_data_before = regression_data["before"]

    boid_posX_b, boid_posY_b, boid_velX_b, boid_velY_b = boid_data_before
    boid_positions_before = (boid_posX_b, boid_posY_b)
    boid_velocities_before = (boid_velX_b, boid_velY_b)

    test_boids_master = BoidsMaster()
    test_boids_master.set_boids(np.array(boid_positions_before),np.array(boid_velocities_before))
    test_boids_master.update_boids()

    boid_posX_a = test_boids_master.positions[0,:].tolist()
    boid_posY_a = test_boids_master.positions[1,:].tolist()
    boid_velX_a = test_boids_master.velocities[0,:].tolist()
    boid_velY_a = test_boids_master.velocities[1,:].tolist()

    boid_data = (boid_posX_a, boid_posY_a, boid_velX_a, boid_velY_a)

    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)

def test_new_boids_fly2center_regression():
    '''
    Regression test - Fly to center method
    '''
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures/fixture_fly2center.yml')))
    boid_data_before = regression_data["before"]

    boid_positions_before, boid_velocities_before = boid_data_before

    test_boids_master = BoidsMaster()
    test_boids_master.set_boids(np.array(boid_positions_before),np.array(boid_velocities_before))
    test_boids_master.fly_towards_center()
    test_boids_master.update_positions()

    boid_positions_after = test_boids_master.positions.tolist()
    boid_velocities_after = test_boids_master.velocities.tolist()

    boid_data = (boid_positions_after, boid_velocities_after)

    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)

def test_new_boids_fly_away_neighbours_regression():
    '''
    Regression test - Fly away from neighbours method
    '''
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures/fixture_fly_away_neighbours.yml')))
    boid_data_before = regression_data["before"]

    boid_positions_before, boid_velocities_before = boid_data_before

    test_boids_master = BoidsMaster()
    test_boids_master.set_boids(np.array(boid_positions_before),np.array(boid_velocities_before))
    test_boids_master.fly_away_from_neighbours()
    test_boids_master.update_positions()

    boid_positions_after = test_boids_master.positions.tolist()
    boid_velocities_after = test_boids_master.velocities.tolist()

    boid_data = (boid_positions_after, boid_velocities_after)
    #
    # print(len(boid_data_before))
    # print(len(boid_velocities_after))

    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)


def test_new_boids_match_speed_regression():
    '''
    Regression test - Match speed with neighbours
    '''
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures/fixture_match_speed.yml')))
    boid_data_before = regression_data["before"]

    boid_positions_before, boid_velocities_before = boid_data_before

    test_boids_master = BoidsMaster()
    test_boids_master.set_boids(np.array(boid_positions_before),np.array(boid_velocities_before))
    test_boids_master.match_speed_w_neighbours()
    test_boids_master.update_positions()

    boid_positions_after = test_boids_master.positions.tolist()
    boid_velocities_after = test_boids_master.velocities.tolist()

    boid_data = (boid_positions_after, boid_velocities_after)

    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)
