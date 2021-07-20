# week 3

---

---

# Circadian Clock

---

- find genes responsible for time
- 3 genes in plants for plants
    - transcription factors
    - find hidden transcription factors binding sites
        - they are many of them
- brute force algorithm for motif finding
- implanted Motif Problem: Find all (k, d)-motifs in a collection of strings.
    - input: a collection of strings Dna, and integers k and d
    - output: all (k, d)-motifs in Dna

```jsx
	MotifEnumeration(Dna, k, d)
        Patterns ← an empty set
        for each k-mer Pattern in the first string in Dna
            for each k-mer Pattern’ differing from Pattern by at most d mismatches
                if Pattern' appears in each string from Dna with at most d mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns
```

- not work
    - bc some genes do not have motif

# Scoring Motifs

---

- Scoring Motifs
    - Profile: percentage
    - Consensus: the most popular letters in each columns
    - score: number of lowercase letters in the matrix

    ![week%203%2006407da311824f9d940ce0bf4450283d/Screen_Shot_2021-07-15_at_2.57.58_PM.png](week%203%2006407da311824f9d940ce0bf4450283d/Screen_Shot_2021-07-15_at_2.57.58_PM.png)

- certain position feature 2 nucleotides with roughly the same ability to bind the transcription factor
    - in the last column, T should also be accepted

## Entropy and the motif logo

- lower the entropy, higher the information content, highly conserved
- motif logo

    ![week%203%2006407da311824f9d940ce0bf4450283d/Screen_Shot_2021-07-15_at_3.54.10_PM.png](week%203%2006407da311824f9d940ce0bf4450283d/Screen_Shot_2021-07-15_at_3.54.10_PM.png)

# Motif Finding Problem

---

- Motif finding problem: Given a collection of strings, find a set of k-mers, one from each string, that minimizes the score of resulting motif.
    - input: A collection of strings Dna and an integer k
    - output: A collection Motifs of k-mers, one from each string in Dna, minimizing Score(Motifs) among all possible choices of k-mers.
- approach: sum of hamming distance between consensus Pattern and each motif. → minimize d(Pattern, Motifs)

### Median String

- input:  A collection of strings Dna and an Integer k
- outputL A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mer

```jsx
MedianString(Dna, k)
        distance ← ∞
        for each k-mer Pattern from AA…AA to TT…TT
            if distance > d(Pattern, Dna)
                 distance ← d(Pattern, Dna)
                 Median ← Pattern
        return Median
```

- find distance between a k-mer and a long string
    - mov along the frame and find min distance between pattern and string
- distance between k-mer and a set of strings
    - sum of distance

### Greedy Approach

- probability

![week%203%2006407da311824f9d940ce0bf4450283d/Screen_Shot_2021-07-18_at_10.52.33_PM.png](week%203%2006407da311824f9d940ce0bf4450283d/Screen_Shot_2021-07-18_at_10.52.33_PM.png)

```jsx
GreedyMotifSearch(Dna, k, t)
        form a set of k-mers BestMotifs by selecting 1st k-mers in each string from Dna
        for each k-mer Motif in the first string from Dna
            Motif1 ← Motif
            for i = 2 to t
                form Profile from motifs Motif1, …, Motifi - 1
                Motifi ← Profile-most probable k-mer in the i-th string in Dna
            Motifs ← (Motif1, …, Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        output BestMotifs
```

### Pseudocounts to Greedy Approach

- Laplace's rule of Succession
    - add 1 to each element of Count(Motifs)

```jsx
GreedyMotifSearch(Dna, k, t)
        form a set of k-mers BestMotifs by selecting 1st k-mers in each string from Dna
        for each k-mer Motif in the first string from Dna
            Motif1 ← Motif
            for i = 2 to t
                apply Laplace's Rule of Succession to form Profile from motifs Motif1, …, Motifi-1
                Motifi ← Profile-most probable k-mer in the i-th string in Dna
            Motifs ← (Motif1, …, Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        output BestMotifs
```