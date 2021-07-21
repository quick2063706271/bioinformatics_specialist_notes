from typing import List, Dict
import random


def form_count_table(motifs: List):
    profile = {'A': [], 'T': [], 'C': [], 'G': []}
    for i in range(len(motifs[0])):
        lst = [motifs[n][i] for n in range(len(motifs))]
        profile['A'].append(lst.count('A'))
        profile['T'].append(lst.count('T'))
        profile['C'].append(lst.count('C'))
        profile['G'].append(lst.count('G'))
    return profile


def form_profile_with_pseudocounts(motifs: List):
    count_table = form_count_table(motifs)
    contains_zero = 0
    for lst in count_table.values():
        if 0 in lst:
            contains_zero = 1
    if contains_zero == 1:
        total = len(motifs) + 4
        for key in count_table.keys():
            for i in range(len(count_table[key])):
                count_table[key][i] += 1
                count_table[key][i] = count_table[key][i] / total   # shit that's so hard
    return count_table


def form_profile(motifs: List):
    profile = {'A': [], 'T': [], 'C': [], 'G': []}
    for i in range(len(motifs[0])):
        lst = [motifs[n][i] for n in range(len(motifs))]
        profile['A'].append(lst.count('A') / len(motifs))
        profile['T'].append(lst.count('T') / len(motifs))
        profile['C'].append(lst.count('C') / len(motifs))
        profile['G'].append(lst.count('G') / len(motifs))
    return profile


def profile_most_probable(text: str, k: int, profile: Dict):
    max_prob = -1
    max_pattern = ''
    for i in range(0, len(text) - k + 1):
        pattern = text[i: i + k]
        prob = 1
        for j in range(len(pattern)):
            prob *= profile[pattern[j]][j]
        if prob > max_prob:
            max_prob = prob
            max_pattern = pattern
    return max_pattern


def motif(profile: Dict, dna: List):
    motifs = []
    for s in dna:
        motifs.append(profile_most_probable(s, len(profile['A']), profile))
    return motifs


def score(motifs: List):
    score = 0
    for i in range(len(motifs[0])):
        lst = [dna[i] for dna in motifs]
        most_common = max(set(lst), key=lst.count)
        score += (len(lst) - lst.count(most_common))
    return score


def randomized_motif_search(dna: List, k: int, t: int):
    random.seed(2017)
    random_int = [random.randint(0, len(dna[0]) - k) for i in range(len(dna))]
    motifs = [dna[i][random_int[i]: random_int[i] + k] for i in range(len(random_int))]
    best_motifs = motifs
    while True:
        profile = form_profile_with_pseudocounts(motifs)
        motifs = motif(profile, dna)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


if __name__ == '__main__':
    dna = [
        'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
        'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
        'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
        'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
        'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'
    ]
    k = 8
    t = 5
    print(randomized_motif_search(dna, 8, 5))
