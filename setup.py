from setuptools import setup, find_packages
import os
import subprocess
from setuptools.command.build_py import build_py

class BuildSovereign(build_py):
    def run(self):
        # 1. Build the Python parts first
        super().run()
        # 2. Compile the NS-33 Engine
        cwd = os.getcwd()
        try:
            bundle_path = os.path.join(cwd, "src_bundle")
            if os.path.exists(bundle_path):
                print("\033[1;34m[KISSAT-SOVEREIGN] Compiling NS-33 Engine...\033[0m")
                os.chdir(bundle_path)
                subprocess.run(["chmod", "+x", "configure"], check=True)
                subprocess.run(["./configure"], check=True)
                subprocess.run(["make"], check=True)
                os.chdir(cwd)
        except Exception as e:
            print(f"Compilation warning: {e}")
            os.chdir(cwd)

setup(
    name="kissat-sovereign",
    version="1.0.3",
    packages=find_packages(include=['sovereign_pkg', 'sovereign_pkg.*']),
    include_package_data=True,
    package_data={'': ['src_bundle/*']},
    cmdclass={'build_py': BuildSovereign},
    entry_points={
        'console_scripts': [
            'kissat-sovereign=sovereign_pkg.engine:main',
        ],
    },
    author="Americo Simoes",
    description="NS-33 Fractal Layer P=NP Solver Bridge",
)
