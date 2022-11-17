class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:
            return n
        
        in_deg = defaultdict(int)
        out_deg = defaultdict(int)
        
        for i in trust:
            in_deg[i[1]] += 1
            out_deg[i[0]] += 1
            
        for i in in_deg:
            if in_deg[i] == n-1:
                if not out_deg[i]:
                    return i
                else:
                    break
            
        return -1