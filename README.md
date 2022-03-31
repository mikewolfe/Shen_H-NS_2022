# Analysis code for Shen et al. 2022 #
This repository contains original code used to analyze data for the Shen et. al.
2022 paper.

Each directory contains a different part of the analysis
- `md_sim_pattern_matching/` contains code to match footprinting and TEN-map
  data against patterns from MD simulations
- `pvalues_calcs/` contains code to generate p-values for how well the MD
  simulation matches the footprinting and TEN-map data
- `modeling/` contains code for using sequence, structure, and electrostatic
  features to predict H-NS DBD binding locations at the bp level
- `compare_ishihama_data/` contains code for checking for enrichment of
  sequence, structure, and electrostatic features in gSELEX data from the
  Ishihama group.

Each directory has it's own `README.md` file describing what it contains and how
to re-run the analysis.

For any specific questions about this code or analysis please contact Michael
Wolfe at mwolfe6@wisc.edu.
