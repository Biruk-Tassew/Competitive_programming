class Solution:
    def appealSum(self, s: str) -> int:
        seen = {s[0]:0}
        count = 1
        prev_cnt = 1
        
        for i in range(1, len(s)):
            if s[i] in seen:
                temp_cnt = prev_cnt + (i-seen[s[i]])
            else:  
                temp_cnt = prev_cnt + (i+1)
                
            prev_cnt = temp_cnt
            count += temp_cnt
            seen[s[i]] = i
            
        return count
                    
            