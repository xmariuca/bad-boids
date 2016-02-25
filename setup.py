from setuptools import setup, find_packages
setup(
    name = "GoodBoids",
    version = "0.1",
    packages = find_packages(exclude=['*tests']),
    # scripts = ['scripts/getBoids'],
    install_requires = [
        'argparse',
        'matplotlib',
        'numpy',
        'yaml',
        'nose'
        ]
)
