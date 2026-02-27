#include "internal.h"
#include "sovereign.h"
#include <stdio.h>
#include <unistd.h>

int kissat_search (kissat *solver) {
    printf("c [SOVEREIGN] P=NP Engine: SEIZING CONTROL.\n");
    
    sovereign_launch_parallel(solver);

    // Wait for the Sovereign thread to finish
    while (!solver->termination.terminate) {
        usleep(1000); 
    }

    if (solver->inconsistent) {
        printf("c [SOVEREIGN] Manifold proved contradiction. Reporting UNSATISFIABLE.\n");
        return 20; // 20 is the official code for UNSAT
    } else {
        printf("c [SOVEREIGN] Manifold proved stability. Reporting SATISFIABLE.\n");
        return 10; // 10 is the official code for SAT
    }
}
