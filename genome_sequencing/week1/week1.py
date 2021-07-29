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
    for i in range(len(patterns) - 1):
        p1 = patterns[i]
        p2 = patterns[i + 1]
        if p1 not in adj_list.keys():
            adj_list[p1] = []
        if p1[1:] == p2[: -1]:
            adj_list[p1].append(p2)
        if len(adj_list[p1]) == 0:
            adj_list.pop(p1)
    return adj_list


def de_bruijin_graph(k: int, text: str):
    composition = string_composition(k - 1, text)
    return overlap_graph(composition)

if __name__ == '__main__':

    print(de_bruijin_graph(2, 'TAATGCCATGGGATGTT'))
    print(de_bruijin_graph(3, 'TAATGCCATGGGATGTT'))
    print(de_bruijin_graph(4, 'TAATGCCATGGGATGTT'))
    print(de_bruijin_graph(3, 'TAATGGGATGCCATGTT'))
