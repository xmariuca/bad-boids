import yaml
from boids_master import BoidsMaster
from copy import deepcopy
import numpy as np


def create_fixture_unit():
    '''
    Creates fixture file for a regression test for the whole clss as an unit.
    '''
    # *******************************************************
    # Write fixture file for the BoidsMaster.fly_towards_center()
    fixt_boids = BoidsMaster()
    before_positions = deepcopy(fixt_boids.positions.tolist())
    before_velocities = deepcopy(fixt_boids.velocities.tolist())
    fixt_boids.update_boids()

    after_positions = fixt_boids.positions.tolist()
    after_velocities = fixt_boids.velocities.tolist()

    before = (before_positions, before_velocities)
    after = (after_positions, after_velocities)

    fixture = {"before": before, "after": after}
    fixture_file = open("tests/fixtures/fixture_general.yml", 'w')
    fixture_file.write(yaml.dump(fixture))
    fixture_file.close()


def create_fixture1():
    '''
    Creates fixture file for testing the flight towards the middle of the flock.
    '''
    # *******************************************************
    # Write fixture file for the BoidsMaster.fly_towards_center()
    fixt_boids = BoidsMaster()
    before_positions = deepcopy(fixt_boids.positions.tolist())
    before_velocities = deepcopy(fixt_boids.velocities.tolist())
    fixt_boids.fly_towards_center()
    fixt_boids.update_positions()

    after_positions = fixt_boids.positions.tolist()
    after_velocities = fixt_boids.velocities.tolist()

    beforeM1 = (before_positions, before_velocities)
    afterM1 = (after_positions, after_velocities)

    fixture = {"before": beforeM1, "after": afterM1}
    fixture_file = open("tests/fixtures/fixture_fly2center.yml", 'w')
    fixture_file.write(yaml.dump(fixture))
    fixture_file.close()


def create_fixture2():
    '''
    Creates fixture file for testing the flight away from newighbouring boids.
    '''
    # *******************************************************
    # Write fixture file for the BoidsMaster.fly_away_from_neighbours()
    fixt_boids = BoidsMaster()
    before_positions = deepcopy(fixt_boids.positions.tolist())
    before_velocities = deepcopy(fixt_boids.velocities.tolist())
    fixt_boids.fly_away_from_neighbours()
    fixt_boids.update_positions()

    after_positions = fixt_boids.positions.tolist()
    after_velocities = fixt_boids.velocities.tolist()

    beforeM2 = (before_positions, before_velocities)
    afterM2 = (after_positions, after_velocities)

    fixture = {"before": beforeM2, "after": afterM2}
    fixture_file = open("tests/fixtures/fixture_fly_away_neighbours.yml", 'w')
    fixture_file.write(yaml.dump(fixture))
    fixture_file.close()


def create_fixture3():
    '''
    Creates fixture file for testing the flight in formation.
    '''
    # *******************************************************
    # Write fixture file for the BoidsMaster.match_speed_w_neighbours()
    fixt_boids = BoidsMaster()
    before_positions = deepcopy(fixt_boids.positions.tolist())
    before_velocities = deepcopy(fixt_boids.velocities.tolist())
    fixt_boids.match_speed_w_neighbours()
    fixt_boids.update_positions()

    after_positions = fixt_boids.positions.tolist()
    after_velocities = fixt_boids.velocities.tolist()

    beforeM3 = (before_positions, before_velocities)
    afterM3 = (after_positions, after_velocities)

    fixture = {"before": beforeM3, "after": afterM3}
    fixture_file = open("tests/fixtures/fixture_match_speed.yml", 'w')
    fixture_file.write(yaml.dump(fixture))
    fixture_file.close()

# *******************************************************
create_fixture1()
create_fixture2()
create_fixture3()
create_fixture_unit()
