class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        word_one_cnt = Counter(word1)
        word_two_cnt = Counter(word2)
        return Counter(word_one_cnt.values()) == Counter(word_two_cnt.values())
        
        
        
        