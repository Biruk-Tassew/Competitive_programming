class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = {}
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        for i in range(len(s)):
            if pattern[i] in word_dict:
                if word_dict[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in word_dict.values():
                    return False
                word_dict[pattern[i]] = s[i]
                
        return True