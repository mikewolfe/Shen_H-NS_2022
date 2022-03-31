# Comparing footprinting, TEN-map, and MD simulations #

In this directory is code to reproduce matching of patterns between MD
simulations and experimental data.

- `md_sim.tsv` has raw cleavage propensity data estimated from the MD
  simulations
- `surface_calc_strand.tsv` has surface accessibility data estimated from the MD
  simulations
- `generate_md_sim_RZ.Rmd` converts the raw MD simulations into robustZ-scaled
  versions of the traces with the specific 15 bp pattern to match
- `tethered_estimates_vector` contains the robustZ-scaled estimates for the
  TEN-map data to match the robustZ-scaled cleavage propensity data against 
  (`pattern_vector_rz.txt`)
- `hydroxy_estimates_vector.txt` contains the robustZ-scaled estimates for the
  OH radical footprinting data to match against the robustZ-scaled surface
  accessibility data from the MD simulations (`OH_pattern_vector_rz.txt`)
- `pattern_match.sh` runs the actual pattern match calculations spitting out
  three files for each match `*_match_scores.tsv` containing the actual match
  scores `*_match_scores_rand.tsv` containing the match scores for randomly
  shuffled data and `*_plot_data.png` giving an image of the experimental data
  for each modality.
- `determine_pattern_match.py` is the python script that runs the matching
  itself
