import kissat_apex
import sys

def verify():
    print("--- Sovereign-Logic 2.0.0-Apex Handshake ---")
    try:
        # We use the hole3.cnf in your directory
        status = kissat_apex.solve_sovereign("hole3.cnf")
        print(f"Node Status: {status}")
    except Exception as e:
        print(f"Decoherence detected: {e}")

if __name__ == "__main__":
    verify()
