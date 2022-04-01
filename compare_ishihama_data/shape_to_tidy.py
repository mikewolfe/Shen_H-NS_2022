import fasta
import sys

if __name__ == "__main__":
    infile = sys.argv[1]
    shape_name = sys.argv[2]

    vals = fasta.FastaFile()

    with open(infile) as inf:
        vals.read_whole_datafile(inf)
    sys.stdout.write("contig\tcoord\tvalue\tparam\n")
    for seq in vals:
        for coord, val in enumerate(seq):
            sys.stdout.write("%s\t%s\t%s\t%s\n"%(seq.chrm_name(), coord, val, shape_name))

