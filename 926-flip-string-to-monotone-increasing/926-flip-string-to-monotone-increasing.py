class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = 0
        
        for i in s:
            if i == "0":
                zeros += 1
                
        
        ans = zeros
        zeros_in_right = zeros
        for i in s:
            if i == "0":
                zeros_in_right -= 1
                ans = min(ans, zeros_in_right)
            else:
                zeros_in_right += 1
                
        return ans
            
        
            