class Anagram:
    def anagram(s: str, t: str) -> bool:
        # scrivere qui il codice
        return sorted(s.lower()) == sorted(t.lower())

    print(anagram("anagram","nagaram"))

    print(anagram("rat", "car"))

    print(anagram("silent","listen"))

    print(anagram("NeurIPS","UniReps"))