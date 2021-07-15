# week 2

## dna has 2 directions

- dna polymerase if unidirectional
- okazaki fragment for foward directions
- forward strand has most of time single stranded
    - single strand has more possibility of mutation
    - C→T often

### G-C

![week%202%2039a4ffdff79845edb40b8b967b2cc175/Screen_Shot_2021-07-03_at_11.32.30_PM.png](week%202%2039a4ffdff79845edb40b8b967b2cc175/Screen_Shot_2021-07-03_at_11.32.30_PM.png)

Forward half-strand has shortage of C and normal G; reverse half strand have a shortage of G and normal C

- IF we find G-C decreasing and suddenly it starts increasing → find origin of replication

### Skew diagram

- Skew(k): #G-#C for the first k nucleotides of Genome.
- Skew diagram:
    - Plot Skew(k) against k
- function to find min of Skew

```python
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
```

### Mismatch problem

- Hamming distance: number of mismatches

```python
def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        return
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance
```

- Approximate Pattern Count

```python
def approx_pattern_count(pattern: str, text: str, d: int):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(pattern, text[i: i + len(pattern)]) <= d:
            count += 1
    return count
```

- find most frequent words with mismatches problem
    - Input: a string Text, integer k and d
    - output: all most frequent k-mers with up to d mismatches in Text

CS

---

- neighborhood for a string
- immediate neighborhood
    - neighborhood with one mismatches

    ```python
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
    ```

- recursive methods
    - (k-1)-mer pattern
        - belongs to neighbors(Suffix(Pattern), d)
            - add FirstSymbol(Pattern) to beginning to obtain k-mer
            - add any symbol to the beginning of Pattern