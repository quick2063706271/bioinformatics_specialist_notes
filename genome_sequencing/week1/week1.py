# String Composition
from typing import List


def string_composition(k: int, text: str):
    lst = []
    for i in range(len(text) - k + 1):
        lst.append(text[i: i + k])
    return lst


# Reconstruct a string from its genome path.
def path_to_genome(patterns: List):
    s = patterns[0][: -1]
    for i in range(0, len(patterns)):
        s += patterns[i][-1]
    return s


# construct the overlap graph of a collection of k-mers
def overlap_graph(patterns: List):
    adj_list = {}
    for p1 in patterns:
        adj_list[p1] = []
        for p2 in patterns:
            if p1[1:] == p2[: -1]:
                adj_list[p1].append(p2)
        if len(adj_list[p1]) == 0:
            adj_list.pop(p1)
    return adj_list


if __name__ == '__main__':
    print(overlap_graph([
        'ATGCG',
        'GCATG',
        'CATGC',
        'AGGCA',
        'GGCAT',
        'GGCAC'
    ]))