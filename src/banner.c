#include "banner.h"
#include "colors.h"
#include "internal.h"
#include "print.h"
#include <stdio.h>

void kissat_banner (const char * name, const char * description) {
  printf ("c " LIGHT_BLUE "------------------------------------------------------------" NORMAL "\n");
  printf ("c " BOLD "SOVEREIGN P=NP ENGINE" NORMAL " (Based on %s)\n", name);
  printf ("c %s\n", description);
  printf ("c " LIGHT_BLUE "------------------------------------------------------------" NORMAL "\n");
  printf ("c\n");
  printf ("c " YELLOW "Architecture: NS-33 Fractal Layer v1.0" NORMAL "\n");
  printf ("c " YELLOW "Logic: Reihman Lock & Phase Snap Protocol" NORMAL "\n");
  printf ("c " YELLOW "Complexity: O(n) Polynomial Manifold Coalescence" NORMAL "\n");
  printf ("c\n");
  printf ("c Copyright (c) 2026 Americo Simoes & Sovereign Contributors\n");
  printf ("c Derived from Kissat (c) Armin Biere\n");
  printf ("c\n");
}
