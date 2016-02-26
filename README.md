# Boids Simulator - Python Package

This Python package creates a simulation of the flocking behaviour of boids. It outputs a window and an .mp4 file with the animated flight.

---

### Dependencies

Libraries used:
* argparse
* numpy
* matplotlib
* yaml
* nose

### Installation

The package can be installed using pip directly from GitHub:

```sh
$ pip install git+https://github.com/xmariuca/bad-boids.git
```

Alternately, the package can be first cloned and installed using:

```sh
$ python setup.py install
```
### Usage

The package can be used:

* as a library by calling the function `main_animate_boids(number_boids, collision_alert, formation_limit, strength2middle, strength2formation)` from  `refactoredBoids.boids_main`

```python
# example usage of the function
main_animate_boids(100, 100, 10000, 0.01, 0.0125)
```
* from the command line 

```sh
$ simulate_boids --number_boids 50 --collision_alert 100 --formation_limit 10000 --strength_to_middle 0.01 --strength_to_formation 0.125

Boids Simulator - generates a flock of birds and simulates its flying behaviour based on the input parameters.

optional arguments:
  -h, --help            show this help message and exit
  --number_boids NUMBER_BOIDS
                        Number of boids, default = 50
  --collision_alert COLLISION_ALERT
                        Collision alert, default = 100
  --formation_limit FORMATION_LIMIT
                        Formation limit, default = 10000
  --strength_to_middle STRENGTH_TO_MIDDLE
                        Strength to flock center, default = 0.01
  --strength_to_formation STRENGTH_TO_FORMATION
                        Strength to formation, default = 0.0125
```

For more information about the functions, please see the commented code.

### Version
1.0.0

### License
MIT

## MPHYG001-coursework2

This package was created as part of the second coursework of the module MPHYG001 - Research Software Engineering with Python.

Author: Maria Ruxandra Robu,
MRes Medical Imaging, University College London 2015-2016

### Assignment task

A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring
