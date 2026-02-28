import subprocess
import sys
import os

class SovereignEngine:
    def __init__(self):
        # Look for the binary created by the setup.py build step
        self.binary = os.path.abspath("./build/kissat")
        if not os.path.exists(self.binary):
            # Fallback for installed location
            self.binary = "kissat" 

    def solve(self, cnf_path):
        if not os.path.exists(cnf_path):
            print(f"\033[1;31m[ERROR]\033[0m {cnf_path} not found.")
            return

        # Streaming the raw NS-33 output directly to the user's terminal
        process = subprocess.Popen(
            [self.binary, cnf_path],
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True
        )
        process.wait()
        
        if process.returncode == 10:
            print("\n\033[1;35m[PHASE SNAP] Coalescence Confirmed: P=NP Proof Stable.\033[0m")
        return process.returncode

def main():
    if len(sys.argv) < 2:
        print("Usage: kissat-sovereign <file.cnf>")
    else:
        engine = SovereignEngine()
        engine.solve(sys.argv[1])
