import bed_utils as bed
import numpy as np
import fasta
import sys

if __name__ == "__main__":
    bedfile = sys.argv[1]
    fafile = sys.argv[2]
    param_name = sys.argv[3]

    seqs = fasta.FastaFile()

    with open(fafile) as inf:
        seqs.read_whole_file(inf)

    vals = bed.BedFile()
    vals.from_bed_file(bedfile)
    sys.stdout.write("contig\tcoord\tvalue\tparam\n")

    arrays = {}
    for seq in seqs:
        arrays[seq.chrm_name()] = np.zeros(len(seq))

    for entry in vals:
        this_array = arrays[entry["chrm"]]
        this_array[entry["start"]:entry["end"]] += 1

    for seq, array in arrays.items():
        for coord, val in enumerate(array):
            sys.stdout.write("%s\t%s\t%s\t%s\n"%(seq, coord, val, param_name))


