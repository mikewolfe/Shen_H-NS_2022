python3 search_by_regex.py Ishihama_sites.fa \
    "(?=(AAAA|AAAT|AATT|ATTT|TTTT))" > Ishihama_atracts.bed

python3 search_by_regex.py Ishihama_sites.fa \
    "(?=(ATAA|ATAT|ATTA|AATA|TAAA|TAAT|TATA|TATT|TTAA|TTAT|TTTA))" > Ishihama_tastep.bed

