from setuptools import setup, find_packages

setup(
    name="sovereign-sat",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sovereign=sovereign_pkg.engine:main',
        ],
    },
    author="Americo Simoes",
    description="NS-33 Fractal Layer P=NP Solver Bridge",
)
