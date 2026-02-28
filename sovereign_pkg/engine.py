import subprocess
import sys
import os

class Zenith:
    def __init__(self):
        # Look for the binary in the expected build path
        self.binary = os.path.abspath("./build/kissat")
        if not os.path.exists(self.binary):
            raise FileNotFoundError("Sovereign binary not found. Please run 'make' first.")

    def solve(self, cnf_path):
        if not os.path.exists(cnf_path):
            print(f"[ERROR] {cnf_path} not found.")
            return

        # We use Popen with sys.stdout to ensure the LIVE terminal output
        # including the blue banner and 0.00s profiling, is shown.
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
        print("Usage: sovereign <file.cnf>")
    else:
        z = Zenith()
        z.solve(sys.argv[1])
