from setuptools import setup, find_packages
setup(
    name = "BoidsSimulator",
    author = "Maria Ruxandra Robu",
    author_email = 'maria.robu.14@ucl.ac.uk',
    license = 'The MIT License (MIT)',
    description = 'A simulator of the flying behaviour of boids',
    url = 'https://github.com/xmariuca/bad-boids.git',
    version = "1.0.0",
    packages = find_packages(exclude=['*tests']),
    scripts = ['scripts/simulate_boids'],
    install_requires = [
        'argparse',
        'matplotlib',
        'numpy',
        'nose'
        ]
)
