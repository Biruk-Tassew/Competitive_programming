class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        start = 0
        
        for word in words:
            if s[start:start+len(word)] != word:
                return False
            
            start += len(word)
            
            if start == len(s):
                return True
            
        return False