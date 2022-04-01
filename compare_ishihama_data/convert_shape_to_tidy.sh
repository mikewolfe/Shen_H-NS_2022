python3 shape_to_tidy.py Ishihama_sites.fa.MGW MGW > Ishihama_shape_tidy.tsv
for SHAPE in "ProT" "EP" "HelT" "Roll";
do
    python3 shape_to_tidy.py Ishihama_sites.fa.${SHAPE} ${SHAPE} | tail -n +2 >> Ishihama_shape_tidy.tsv;
done




