import regex
import sys
import fasta
import bed_utils

def find_matches(seq, reg, outbed):
    ## THIS IS WRITTEN TO DEAL WITH A LOOK AHEAD GROUP FOR OVERLAPPING MATCHES
    ## I.E. "(?=(alskdjfa;sldkjf))"
    matches = reg.finditer(this_seq)
    for match in matches:
        start = match.span()[0]
        match_seq = match.group(1)
        end = start + len(match_seq)
        this_entry = bed_utils.BedEntry([chrm.chrm_name(),
            start,
            end,match_seq])

        outbed.add_entry(this_entry)
    return outbed


if __name__ == "__main__":

    inseq = sys.argv[1]
    reg = sys.argv[2]

    reg = regex.compile(reg)

    genome = fasta.FastaFile()
    outbed = bed_utils.BedFile()
    with open(inseq) as inf:
        genome.read_whole_file(inf)

    for chrm in genome:
        this_seq = chrm.seq
        find_matches(this_seq, reg, outbed)


    outbed.write_bed_file(1)




