import sys
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(pattern, d_slice):
    return np.sqrt(np.sum((pattern - d_slice)**2))

def manhattan_distance(pattern, d_slice):
    return np.sum(abs(pattern - d_slice))

def get_distance_vector(pattern, data):
    distances = []
    pattern_size = pattern.shape[1]
    data_length = data.shape[1]
     
    for val in range(0 + int(pattern_size/2), data_length - int(pattern_size/2), 1):
        distances.append(
                manhattan_distance(pattern, data[:,val-int(pattern_size/2):val+int(pattern_size/2)+1])
                )
    return(np.array(distances))

def write_data(dat, fhandle, direction = "forward"):
    for i, val in enumerate(dat):
        fhandle.write("%d\t%f\t%s\n"%(i, val, direction))

def shuffle_blocks(d, size_blocks):
    blocked = []
    for block_start in range(0, d.shape[1], size_blocks):
        if block_start + size_blocks > d.shape[1]:
            blocked.append(d[:,block_start:])
        else:
            blocked.append(d[:,block_start:block_start+size_blocks])
    np.random.shuffle(blocked)
    return(np.hstack(blocked))

if __name__ == "__main__":
    # ASSUMES PATTERN IS AN ODD NUMBER OF BASES AND IS IN A SINGLE VECTOR WITH DATA FOR EACH STRAND ONE AFTER THE OTHER
    # ASSUMES DATA IS IN A SINGLE VECTOR WITH TEMPLATE AND NON-TEMPLATE ONE AFTER THE OTHER
    pattern = sys.argv[1]
    data = sys.argv[2]
    name = sys.argv[3]
    shuffle_size = int(sys.argv[4])

    np.random.seed(42)
    # load data in
    d = np.loadtxt(data)
    p = np.loadtxt(pattern)
    
    # get data into matrices
    d = np.reshape(d, (2, int(len(d)/2)))
    plt.figure()
    plt.plot(d.transpose())
    plt.savefig("%s_plot_data.png"%(name))
    
    p = np.reshape(p, (2, int(len(p)/2)))
    
    p_flipped = np.fliplr(p)
    
    # forward search
    forward = get_distance_vector(p, d)
    # reverse search
    reverse = get_distance_vector(p_flipped, d)
    with(open("%s_match_scores.tsv"%(name), mode = "w")) as outf:
        outf.write("bp\tmatch_score\tdirection\n")
        write_data(forward, outf, direction = "fwd")
        write_data(reverse, outf, direction = "rev")

    # now sample
    forwards = []
    rand_scores = open("%s_match_scores_rand.tsv"%(name), mode = "w")
    reverses = []

    rand_scores.write("bp\tmatch_score\tdirection\n")
    for i in range(0, 1000):
        ds = shuffle_blocks(d, shuffle_size)
        rand_forward = get_distance_vector(p, ds)
        rand_reverse = get_distance_vector(p_flipped,ds)
        write_data(rand_forward, rand_scores, direction = "fwd_%d"%(i))
        write_data(rand_reverse, rand_scores, direction = "rev_%d"%(i))
    rand_scores.close()
