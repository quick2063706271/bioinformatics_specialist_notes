def reverse_complement(s: str):
    reversed_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    r = ''
    for i in range(len(s)):
        r = reversed_map[s[i]] + r
    return r
    

def skew(text: str):
    n = 0
    skew_lst = [n]
    for i in range(len(text)):
        if text[i] == 'G':
            n += 1
        elif text[i] == 'C':
            n -= 1
        skew_lst.append(n)
    index_list = [i for i in range(len(skew_lst)) if skew_lst[i] == min(skew_lst)]
    return index_list


def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        return
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance


def approx_pattern_matching(pattern: str, text: str, d: int):
    index_lst = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(pattern, text[i: i + len(pattern)]) <= d:
            index_lst.append(i)
    return index_lst


def approx_pattern_count(pattern: str, text: str, d: int):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(pattern, text[i: i + len(pattern)]) <= d:
            count += 1
    return count


def immediate_neighbors(pattern: str):
    neighborhood = set()
    neighborhood.add(pattern)
    for i in range(len(pattern)):
        symbol = pattern[i]
        for x in 'ACTG':
            if x != symbol:
                neighbor = pattern[: i] + x + pattern[i + 1:]
                neighborhood.add(neighbor)
    return neighborhood


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


def frequent_words_with_mismatches(text: str, k: int, d: int):
    patterns = []
    freq_map = {}
    n = len(text)
    for i in range(0, n - k + 1):
        pattern = text[i: i + k]
        neighborhood = list(neighbors(pattern, d))
        for j in range(0, len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freq_map.keys():
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1
    m = max(freq_map.values())
    for pattern in freq_map.keys():
        if freq_map[pattern] == m:
            patterns.append(pattern)
    return patterns


def frequent_words_with_mismatches_freq_map(text: str, k: int, d: int):
    freq_map = {}
    n = len(text)
    for i in range(0, n - k + 1):
        pattern = text[i: i + k]
        neighborhood = list(neighbors(pattern, d))
        for j in range(0, len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freq_map.keys():
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1
    return freq_map


def frequent_words_with_mismatches_and_reversed(text: str, k: int, d: int):
    patterns = []
    freq_map = {}
    n = len(text)
    for i in range(0, n - k + 1):
        pattern = text[i: i + k]
        neighborhood = list(neighbors(pattern, d))
        for j in range(0, len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freq_map.keys():
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1
            reversed_neighbor = reverse_complement(neighbor)
            if reversed_neighbor in freq_map.keys():
                freq_map[reversed_neighbor] += 1
            else:
                freq_map[reversed_neighbor] = 1
    m = max(freq_map.values())
    for pattern in freq_map.keys():
        if freq_map[pattern] == m:
            patterns.append(pattern)
    return patterns
