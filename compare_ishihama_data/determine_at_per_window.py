import sys
import fasta as fa

def windowed_at_content(seq, size):
    if size % 2 == 0:
        raise ValueError("Must be odd window size")
    start_i = 0
    end_i = start_i + size
    while end_i <= len(seq):
        this_seq = seq[start_i:end_i]
        yield (start_i + int((size-1) /2), (this_seq.count("A") + this_seq.count("T"))/size)
        start_i += 1
        end_i = start_i + size


if __name__ == "__main__":
    infasta = sys.argv[1]
    window_size = int(sys.argv[2])
    
    genome = fa.FastaFile()
    with open(infasta) as inf:
        genome.read_whole_file(inf)
    sys.stdout.write("contig\tcoord\tvalue\tparam\n")
    for chrm in genome:
        for (pos, val) in windowed_at_content(chrm.seq, window_size):
            sys.stdout.write("%s\t%s\t%s\t%s\n"%(chrm.chrm_name(), pos, val, "A/T_%sbp"%window_size))

        
