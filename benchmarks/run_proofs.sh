#!/bin/bash
SOLVER="../build/kissat-sovereign"

echo "--- [ Proof 1: 128-bit Adder Stability ] ---"
$SOLVER --probe=0 --eliminate=0 --reduce=0 01_stability_adder.cnf | grep -E "SOVEREIGN|result"

echo -e "\n--- [ Proof 2: Pigeonhole Frustration (UNSAT) ] ---"
$SOLVER --probe=0 --eliminate=0 --reduce=0 02_frustration_pigeonhole.cnf | grep -E "SOVEREIGN|result"

echo -e "\n--- [ Proof 3: Square Root Coalescence ] ---"
$SOLVER --probe=0 --eliminate=0 --reduce=0 03_coalescence_sqrt.cnf | grep -E "SOVEREIGN|result"
