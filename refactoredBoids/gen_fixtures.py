import yaml
from boids_master import BoidsMaster
from copy import deepcopy
import numpy as np

fixt_boids = BoidsMaster()

before_positions = deepcopy(fixt_boids.positions.tolist())
before_velocities = deepcopy(fixt_boids.velocities.tolist())

fixt_boids.update_boids()

after_positions = fixt_boids.positions.tolist()
after_velocities = fixt_boids.velocities.tolist()

before = (before_positions, before_velocities)
after = (after_positions, after_velocities)

fixture = {"before" : before, "after" : after}
fixture_file = open("tests/fixtures/fixture_class.yml",'w')
fixture_file.write( yaml.dump(fixture) )
fixture_file.close()
