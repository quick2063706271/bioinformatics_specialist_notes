def reverse_complement(s: str):
    reversed_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    r = ''
    for i in range(len(s)):
        r = reversed_map[s[i]] + r
    return r

def find_most_frequent_k(s: str, k: int):
    count = {}
    for i in range(0, len(s) - k):
        sub = s[i: i + k]
        if sub not in count.keys():
            count[sub] = 0
        count[sub] += 1
    freq = 0
    substring = ''
    for sub in count.keys():
        if count[sub] > freq:
            substring = sub
            freq = count[sub]
    return substring


def pattern_count(text: str, pattern: str):
    count = 0
    for i in range(0, len(text) - len(pattern)):
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count


def frequency_table(text: str, k: int):
    count = {}
    for i in range(0, len(text) - k):
        sub = text[i: i + k]
        if sub not in count.keys():
            count[sub] = 1
        count[sub] += 1
    return count


def better_frequent_words(text: str, k: int):
    frequent_pattern = []
    fre_map = frequency_table(text, k)
    max_fre = max(fre_map, key=fre_map.get)
    for key in fre_map.keys():
        if fre_map[key] == fre_map[max_fre]:
            frequent_pattern.append(key)
    return frequent_pattern


def find_reverse_complementary(text: str):
    new = ''
    reverse_table = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for i in range(0, len(text)):
        new += reverse_table[text[len(text) - 1 - i]]
    return new


def pattern_search(text: str, pattern: str):
    result = []
    for i in range(0, len(text) - len(pattern)):
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


def find_clumps(text: str, k: int, l: int, t: int):
    patterns = []
    n = len(text)
    for i in range(n - l):
        window = text[i: i + l]
        freq_map = frequency_table(window, k)
        for key in freq_map.keys():
            if freq_map[key] >= t:
                patterns.append(key)
    return list(set(patterns))  # use set to make all elements unique

