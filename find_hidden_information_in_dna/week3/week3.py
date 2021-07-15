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


if __name__ == "__main__":
    Motifs1 = [
        "TCGGGGGTTTTT",
        "CCGGTGACTTAC",
        "ACGGGGATTTTC",
        "TTGGGGACTTTT",
        "AAGGGGACTTCC",
        "TTGGGGACTTCC",
        "TCGGGGATTCAT",
        "TCGGGGATTCCT",
        "TAGGGGAACTAC",
        "TCGGGTATAACC"
    ]

    print(entropy(Motifs1))