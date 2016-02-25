import yaml
from boids_master import BoidsMaster
from copy import deepcopy
import numpy as np

fixt_boids = BoidsMaster()
init_boid_positions = fixt_boids.positions
init_boid_velocities = fixt_boids.velocities
before_positions = deepcopy(init_boid_positions.tolist())
before_velocities = deepcopy(init_boid_velocities.tolist())

# *******************************************************
# Write fixture file for the BoidsMaster.fly_towards_center()
fixt_boids.set_boids(init_boid_positions,init_boid_velocities)
fixt_boids.fly_towards_center()
fixt_boids.update_positions()

after_positions = fixt_boids.positions.tolist()
after_velocities = fixt_boids.velocities.tolist()

before = (before_positions, before_velocities)
after = (after_positions, after_velocities)

fixture = {"before" : before, "after" : after}
fixture_file = open("tests/fixtures/fixture_fly2center.yml",'w')
fixture_file.write( yaml.dump(fixture) )
fixture_file.close()
# *******************************************************
# Write fixture file for the BoidsMaster.fly_away_from_neighbours()
fixt_boids.set_boids(init_boid_positions,init_boid_velocities)
fixt_boids.fly_away_from_neighbours()
fixt_boids.update_positions()

after_positions = fixt_boids.positions.tolist()
after_velocities = fixt_boids.velocities.tolist()

before = (before_positions, before_velocities)
after = (after_positions, after_velocities)

fixture = {"before" : before, "after" : after}
fixture_file = open("tests/fixtures/fixture_fly_away_neighbours.yml",'w')
fixture_file.write( yaml.dump(fixture) )
fixture_file.close()
# *******************************************************
# Write fixture file for the BoidsMaster.match_speed_w_neighbours()
fixt_boids.set_boids(init_boid_positions,init_boid_velocities)
fixt_boids.match_speed_w_neighbours()
fixt_boids.update_positions()

after_positions = fixt_boids.positions.tolist()
after_velocities = fixt_boids.velocities.tolist()

before = (before_positions, before_velocities)
after = (after_positions, after_velocities)

fixture = {"before" : before, "after" : after}
fixture_file = open("tests/fixtures/fixture_match_speed.yml",'w')
fixture_file.write( yaml.dump(fixture) )
fixture_file.close()
# *******************************************************
