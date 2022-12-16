class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        needed = 0
        
        for i in s_count:
            if i not in t_count:
                needed += s_count[i]
            elif s_count[i] > t_count[i]:
                needed += s_count[i] - t_count[i]
            
        for i in t_count:
            if i not in s_count:
                needed += t_count[i]
            elif t_count[i] > s_count[i]:
                needed += t_count[i] - s_count[i]
                
        return needed