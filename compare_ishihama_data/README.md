# Testing for enrichment of H-NS bound features in gSELEX data #

This directory contains code to test for enrichment of key features that are
associated with H-NS binding in previously gathered H-NS gSELEX data from the
Ishihama group. In addition, it contains code used to calculate each feature for
both gSELEX data and the bgl sequence in the paper.

## Binding sites and generation of random sites ##
- `FEMSRE_binding_sites.txt` locations of H-NS gSELEX peaks from the Ishihama
  group
- `Ishihama_H-NS_sites.bed` 101 bp padded H-NS binding sites generated using
  `FEMSRE_binding_sites.txt` as input and the `make_windows.Rmd` notebook.
- `Ishihama_sites_true.bed` same as Ishihama_H-NS_sites.bed with unique names
  for each site
- `Ishihama_sites_rand.bed` randomly sampled sites of the same size from the
  E coli genome
- `create_fire_input.py` generates the `*_true.bed` and `*_rand.bed` files using
  `Ishihama_H-NS_sites.bed` and `U00096.2.fa` (not included but can be
  downloaded from NCBI) files.
- `generate_random_seqs.sh` exact command used to generate `*true.bed` and
  `*rand.bed` files as well as `Ishihama_sites.fa`
- `Ishihama_sites.fa` sequences that correspond to `*rand.bed` and `*true.bed`

## Windowed A/T content ##
- `get_at_per_window.sh` command to get A/T content across `Ishihama_sites.fa`
  at a 5 bp window
- `determine_at_per_window.py` script to calculate windowed A/T content
- `Ishihama_windowed_at.tsv.gz` output of windowed A/T calculations gzipped
  after generation

## TA-steps and A-tracts ##
- `get_at_content_per_step.sh` command to get TA-steps and A-tracts from
  `Ishihama_sites.fa`
- `search_by_regex.py` script to find TA-steps and A-tracts
- `Ishihama_tastep.bed` all identified TA-steps in true and random sites
- `Ishihama_atracts.bed` all identified A-tracts in true and random sites
- `convert_seq_to_tidy.sh` command to convert `tastep.bed` and `atracts.bed` to
  a tidy combined dataframe with per bp counts of sites `tidy_seq_data.tsv.gz`
- `bed_to_tidy.py` script to convert bed files to a tidy dataframe
- `tidy_seq_data.tsv.gz` combined dataframe for TA-steps and A-tracts per bp

## Structural and electrostatic data ##
- `get_shape_data.R` takes `Ishihama_sites.fa` and generates shape data using
  DNAshapeR. Raw output data not included due to large size.
- `convert_shape_to_tidy.sh` command to convert raw SHAPE data into a tidy
  dataframe and outputs `tidy_seq_data.tsv`
- `shape_to_tidy.py` python script to convert raw SHAPE data into a tidy
  dataframe
- `Ishihama_shape_tidy.tsv.gz` - final tidy shape data, gzipped after generation

## Enrichment calculations ##
- `look_at_sequence_data.Rmd` notebook used to calculated enrichment of features
  in the Ishihama gSELEX data
- `Ishihama_feature_enrichment.pdf` final enrichment figure

## Custom helper modules ##
Each of these modules are used by other python scripts in the directory. If you
want to use the other python scripts you will need these python modules in the
same directory
- `fasta.py` helps with manipulation of fasta files
- `bed_utils.py` helps with manipulation of bed files
- `intervaltools.py` helps with interval calculations
