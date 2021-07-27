# week 4

---

---

# Randomized algorithm

---

- Las Vegas Algorithm
- Monte Carlo algorithm

## randomized motif search

---

- dnas are not uniform since there are motifs
    - it creates biased profile
    - as long as we catch it by chance, randomized motif search will lead us t it
- Motifs(Profile, Dna)
- return the motifs by profile and Dna using most probable

```jsx
RandomizedMotifSearch(Dna, k, t)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        BestMotifs ← Motifs
        while forever
            Profile ← Profile(Motifs)
            Motifs ← Motifs(Profile, Dna)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
            else
                return BestMotifs
```

## Gibbs Sampling

---

- replace a single k-mer at each iteration and thus moves with more caution in the space of all motifs
- steps:
1. Form motifs by randomly selecting a k-mer in each sequence
2. randomly choose 1 of the selected k-mers and remove it from motifs
3. crate profile from the remaining k-mers in motifs
4. for each k-mer in RemovedSequence, calculate Pr(k-mer | Profile) resulting in n-k+1 probabilities: p1,p2,...,pn-k+1
5. Roll a dice where probability of ending up at side i is proportional to pi
6. choose a new starting position based on rolling the die. Add the k-mer starting this position in RemovedSequence to motifs
7. Repeat steps 2-6

```jsx
GibbsSampler(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        BestMotifs ← Motifs
        for j ← 1 to N
            i ← Random(t)
            Profile ← profile matrix constructed from all strings in Motifs except for Motifi
            Motifi ← Profile-randomly generated k-mer in the i-th sequence
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
```

---

Conclusion:

- may converge to suboptimal solution
- may reaches local optimum

# Tuberculosis bacteria

---

- caused by Mycobacterium tuberculosis (MTP)

## transition from latent to active

---

- form spores (sporulation) to survive tough condition
- oxygen shortage
- 25 genes activated when it goes to latent

### problem

- we dont know the size of motif (k)