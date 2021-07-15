# week 1

## origin of replication

- hidden message helps e.coli to start of replication
    - DnaA box to bind to start replication

---

- count(Text, Pattern)
    - number of times that a k-mer pattern appears as a substring of Text

    ```jsx
    PatternCount(Text, Pattern)
            count ← 0
            for i ← 0 to |Text| − |Pattern|
                if Text(i, |Pattern|) = Pattern
                    count ← count + 1
            return count
    ```

    - runtime: (|Text|-k+1)*k
- Finding most frequent k-mers in a string.   Input: string output: most frequent k-mers in Text
    1. naive brutal force algorithm

    ```jsx
    FrequentWords(Text, k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← the k-mer Text(i, k)
            Count(i) ← PatternCount(Text, Pattern)
        maxCount ← maximum value in array Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                add Text(i, k) to FrequentPatterns
        remove duplicates from FrequentPatterns
        return FrequentPatterns
    ```

    - runtime: (|Text|-k+1) * runtime of PatternCount = (|Text|-k+1) * (|Text|-k+1)*k

    2. Frequent words approach

    - create a frequency table
    - Then use key to find freq in the map

    ```jsx
    FrequencyTable(Text, k)
        freqMap ← empty map
        n ← |Text|
        for i ← 0 to n − k
            Pattern ← Text(i, k)
            if freqMap[Pattern] doesn't exist
                freqMap[Pattern]← 1
            else
               freqMap[pattern] ←freqMap[pattern]+1 
        return freqMap
    ```

    ```jsx
    BetterFrequentWords(Text, k)
        FrequentPatterns ← an array of strings of length 0
        freqMap ← FrequencyTable(Text, k)
        max ← MaxMap(freqMap)
        for all strings Pattern in freqMap
            if freqMap[pattern] = max
                append Pattern to frequentPatterns
        return frequentPatterns
    ```

---

### Clump Finding

- Formal: A k-mer forms an **(L, t)-clump** inside Genome if there is a short (length L) interval of Genome in which it appears many(at least t ) times
- Clump Finding Problem
    - input: a string genome, and integers k, L and t.
    - Output: All distinct k-mers forming (L, t)-clumps in Genome

```jsx
FindClumps(Text, k, L, t)
    Patterns ← an array of strings of length 0
    n ← |Text|
    for every integer i between 0 and n − L
        Window ← Text(i, L)
        freqMap ← FrequencyTable(Window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t
                append s to Patterns
    remove duplicates from Patterns
    return Patterns
```