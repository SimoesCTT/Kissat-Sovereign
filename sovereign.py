import subprocess
import sys
import os

class Sovereign:
    def __init__(self):
        self.binary = "./build/kissat"
        if not os.path.exists(self.binary):
            print("[ERROR] Binary not found. Run 'make' first.")
        else:
            print("\033[1;34m[SOVEREIGN]\033[0m Bridge Active. NS-33 Fractal Layer Connected.")

    def read(self, path):
        self.current_file = path

    def solve(self):
        if not hasattr(self, 'current_file') or not self.current_file:
            return "No file loaded."
        
        # We use subprocess.Popen to stream the LIVE output to your screen
        # This keeps the "Singapore Zenith" banner visible
        process = subprocess.Popen(
            [self.binary, self.current_file],
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        process.wait()

        # Kissat Exit Codes: 20 = UNSAT, 10 = SAT
        if process.returncode == 20:
            return "\033[1;31mUNSATISFIABLE\033[0m"
        elif process.returncode == 10:
            return "\033[1;32mSATISFIABLE\033[0m"
        else:
            return f"ERROR (Code {process.returncode})"

if __name__ == "__main__":
    solver = Sovereign()
    solver.read("hole12.cnf")
    result = solver.solve()
    print(f"\n[FINAL RESULT] {result}")
