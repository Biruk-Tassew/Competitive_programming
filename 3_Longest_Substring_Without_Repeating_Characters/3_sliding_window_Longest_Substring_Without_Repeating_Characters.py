class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        outPut = 0
        for i in range(len(s)):
            appeared = [0]*256
            for j in range(i, len(s)):
                if appeared[ord(s[j])]:
                    break
                else:
                    outPut = max(outPut, j-i+1)
                    appeared[ord(s[j])] = True
                    
            appeared[ord(s[j])] = False
            
        return outPut
        
