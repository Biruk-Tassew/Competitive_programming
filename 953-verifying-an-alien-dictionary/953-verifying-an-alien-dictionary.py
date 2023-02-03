class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.alphabet = order
        if words == sorted(words, key=self.alien_sort):
            return True
        else:
            return False

    def alien_sort(self, word):
        result = []
        for letter in word:
            result.append(self.alphabet.index(letter))
        return result