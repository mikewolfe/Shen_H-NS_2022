# Predicting H-NS DBD binding at the bp-level #

This directory contains code used to generate logistic regression models to
predict H-NS binding from sequence, structural, and electrostatic features.

- `2022_model_HNS_footprinting.Rmd` this contains the code to perform all
  modeling for the paper
- `*.tsv` are precomputed input feature files calculated using `all_seqs.fa` and
  the feature calculation scripts described in `compare_ishihama_data/`
- `all_seq.fa` contains sequence information for the sequence in this study as
  well as other sequences that have been previously used to study H-NS binding
