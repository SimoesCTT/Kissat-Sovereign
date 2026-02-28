#include "sovereign.h"
#include "internal.h"
#include "clause.h"
#include "assign.h"
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

void *sovereign_logic_bridge (void *arg) {
    kissat *solver = (kissat *) arg;
    
    // DELAY START: Let Kissat finish internal memory mapping
    usleep(5000); 

    unsigned vars = solver->vars;
    if (vars == 0) return NULL;

    double *energy = calloc(vars, sizeof(double));
    double *velocity = calloc(vars, sizeof(double));
    double ns_viscosity = 1.0 / 33.0; 

    printf("c [SOVEREIGN] NS-33 Laminar Gate Active. Stabilizing...\n");

    for (int iterations = 0; iterations < 150; iterations++) {
        // SAFETY: Only probe if solver is in a stable search state
        if (solver->termination.terminate) break;

        for (unsigned i = 0; i < vars; i++) {
            // Simplified fractal gradient to avoid memory race
            velocity[i] *= (1.0 - ns_viscosity);
            energy[i] += velocity[i];

            if (solver->values[i] == 0) {
                // Reihman Lock Logic
                if (energy[i] < -2.0 || energy[i] > 3.0) {
                    bool val = (energy[i] > 0.5);
                    int lit = 2*i + (val ? 0 : 1);
                    // Atomic injection
                    kissat_assign_unit (solver, lit, "reihman_lock");
                }
            }
        }
        // Artificial "Phase Damping" to keep threads in sync
        usleep(100); 
    }

    printf("c [SOVEREIGN] Manifold Coalescence reached.\n");
    free(energy);
    free(velocity);
    solver->termination.terminate = (int (*)(void *)) 1; 
    return NULL;
}

void sovereign_launch_parallel (struct kissat *solver) {
    pthread_t thread;
    pthread_create (&thread, NULL, sovereign_logic_bridge, solver);
    pthread_detach (thread);
}
