import week3
import week4

# Mycobacterium tuberculosis (MTB) can persist in a latent state in humans for many years before causing disease.
# Latency has been found to be linked to hypoxia (lack  of oxygen) in the host. You suspect that genes that are
# activated in  hypoxia are regulated by a common transcription factor, so you collect  the upstream sequences
# for all of the MTB genes that are upregulated in  hypoxia, looking for the motif that corresponds to the binding
# site for  the transcription factor regulating these genes. Your biologist  colleague tells you that you should look
# at the 250 bp upstream region  of each gene (which have been conveniently compiled for you in a FASTA file named
# upstream250.txt -- right click and download this file). Your colleague also tells you that the motif is probably
# about 20 bp long.

if __name__ == '__main__':
    file = open('./upstream250.txt')
    dna = []
    lines = file.readlines()
    for line in lines:
        if line[0] != '>':
            dna.append(line[: -1])

    k = 20
    t = len(dna)
    best_score = 1000000000
    best_motif = ''
    for start in range(20):
        motifs = week4.gibbs_sampler(dna, k, t, 100)
        if week4.score(motifs) < best_score:
            best_score = week4.score(motifs)
            best_motif = motifs
    print(best_motif)
    m1 = week4.randomized_motif_search(dna, k, t)
    m2 = week3.median_string(k, dna)


