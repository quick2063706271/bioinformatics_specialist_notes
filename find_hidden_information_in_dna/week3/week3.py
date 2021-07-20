from typing import List, Dict
import math


def motif_enumeration(dnas: List[str], k: int, d: int):
    patterns = set()
    for i in range(0, len(dnas[0]) - k + 1):
        pattern = dnas[0][i: i+k]
        d_patterns = list(neighbors(pattern, d))
        for d_pattern in d_patterns:
            exist = 1
            for j in range(1, len(dnas)):
                dna_patterns = patterns_with_mismatches(dnas[j], k, d)
                if d_pattern not in dna_patterns:
                    exist = 0
            if exist == 1:
                patterns.add(d_pattern)
    return list(patterns)


def patterns_with_mismatches(dna: str, k: int, d:int):
    patterns = set()
    for i in range(0, len(dna) - k + 1):
        pattern = dna[i: i + k]
        patterns = patterns.union(neighbors(pattern, d))
    return list(patterns)


def neighbors(pattern: str, d) -> set:
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'T', 'C', 'G'}
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for n in 'ATCG':
                neighborhood.add(n+text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood


def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        return
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance


def entropy(dnas: List[str]) -> float:
    probability_table = prob_table(dnas)
    entro = 0.0
    for dna in probability_table:
        for key in dna.keys():
            prob = float(dna[key]) / len(dnas)
            if prob > 0:
                entro += prob * math.log(prob, 2)
    return -entro


def prob_table(dnas: List[str])-> List[Dict]:
    lst = [None] * len(dnas[0])
    for i in range(len(dnas[0])):
        prob = {'A': 0, 'T': 0, "C": 0, "G": 0}
        for j in range(len(dnas)):
            prob[dnas[j][i]] += 1
        lst[i] = prob
    return lst


def median_string(k: int, dna: List[str]):
    median = ''
    kmers = list(kmer_generator(k))
    distance = distancebetweenPatternStrings(kmers[0], dna)
    for i in range(1, len(kmers)):
        if distance > distancebetweenPatternStrings(kmers[i], dna):
            distance = distancebetweenPatternStrings(kmers[i], dna)
            median = kmers[i]
    return median


def distancebetweenPatternStrings(pattern: str, strings: List[str]):
    distance = 0
    for string in strings:
        distance += min_hamming(pattern, string)
    return distance


def min_hamming(pattern: str, string: str):
    min_distance = hamming_distance(string[0: len(pattern)], pattern)
    for i in range(1, len(string) - len(pattern) + 1):
        curr_distance = hamming_distance(string[i: i + len(pattern)], pattern)
        if curr_distance < min_distance:
            min_distance = curr_distance
    return min_distance


def kmer_generator(k):
    kmers = ['']
    for i in range(k):
        for element in set(kmers):
            kmers.append(element + 'A')
            kmers.append(element + 'T')
            kmers.append(element + 'C')
            kmers.append(element + 'G')
            kmers.remove(element)
    return set(kmers)


def form_profile(motifs: List):
    profile = {'A': [], 'T': [], 'C': [], 'G': []}
    for i in range(len(motifs[0])):
        lst = [motifs[n][i] for n in range(len(motifs))]
        profile['A'].append(lst.count('A') / len(motifs))
        profile['T'].append(lst.count('T') / len(motifs))
        profile['C'].append(lst.count('C') / len(motifs))
        profile['G'].append(lst.count('G') / len(motifs))
    return profile


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


def greedy_motif_search(dna: List, k: int, t):
    best_motifs = [item[0: k] for item in dna]
    for i in range(len(dna[0]) - k):
        kmer = dna[0][i: i + k]
        motifs = [kmer]
        for j in range(1, t):
            profile = form_profile(motifs)
            motif_i = profile_most_probable(dna[j], k, profile)
            motifs.append(motif_i)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


def greedy_motif_search_with_pseudocounts(dna: List, k: int, t):
    best_motifs = [item[0: k] for item in dna]
    for i in range(len(dna[0]) - k):
        kmer = dna[0][i: i + k]
        motifs = [kmer]
        for j in range(1, t):
            profile = form_profile_with_pseudocounts(motifs)
            motif_i = profile_most_probable(dna[j], k, profile)
            motifs.append(motif_i)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


def score(motifs: List):
    score = 0
    for i in range(len(motifs[0])):
        lst = [dna[i] for dna in motifs]
        most_common = max(set(lst), key=lst.count)
        score += (len(lst) - lst.count(most_common))
    return score



if __name__ == "__main__":
    dna = [
        'GGCGTTCAGGCA',
        'AAGAATCAGTCA',
        'CAAGGAGTTCGC',
        'CACGTCAATCAC',
        'CAATAATATTCG'
    ]
    print(greedy_motif_search_with_pseudocounts(dna, 3, 5))