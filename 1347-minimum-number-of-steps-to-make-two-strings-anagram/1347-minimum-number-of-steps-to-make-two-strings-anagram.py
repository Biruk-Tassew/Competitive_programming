class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_count = Counter(t)
        s_count = Counter(s)
        needed = 0
        
        for i in s_count:
            if t_count[i] < s_count[i]:
                needed += s_count[i]-t_count[i]
                
        return needed