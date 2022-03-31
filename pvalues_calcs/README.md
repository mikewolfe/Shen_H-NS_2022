# Generating p-values from MD match scores #
In this directory is code to take the raw MD match scores for each experiment
and convert them to p-values.

- `combine_manhattan.Rmd` has code to take the match scores for each
  experiment and convert them to p-values. Additionally it also generates
  combined predictions for an overall picture of H-NS DBD binding
- `combined_individ_binding.tsv` is the output file used for the logistic
  regression modeling in `modeling/`. It is created by `combine_manhattan.Rmd`
  and is the result of considering any location with a pvalue < 0.05 in either
  modality 
- `match_score_p_values_plots.pdf` is a visualization of the p-values over the
  H-NS sequence
- `tenmap_md_percentiles_plot.pdf` is an example percentile plot for looking at
  how the actual match scores differ from the random match scores
