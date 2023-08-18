class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        seen = set()
        left = 0
        right = 9
        
        while right < len(s):
            if s[left:right+1] in seen:
                ans.add(s[left:right+1])
                
            seen.add(s[left:right+1])
            
            left += 1
            right += 1
            
        return ans