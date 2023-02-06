class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.word_dict = set(words)
        self.memo = defaultdict(lambda: -1)
        
        max_len = 1
        for i in words:
            max_len = max(max_len, self.solve(i))
            
        return max_len
    
    
    def solve(self, word):
        if self.memo[word] != -1:
            return self.memo[word]
        
        max_len = 0
        for i in range(len(word)):
            prev_word = word[:i] + word[i+1:]
            if prev_word in self.word_dict:
                max_len = max(max_len, self.solve(prev_word))
                
        self.memo[word] = max_len + 1
        return self.memo[word]