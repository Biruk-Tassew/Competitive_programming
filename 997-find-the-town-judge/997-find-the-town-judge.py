class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        
        count = defaultdict(int)
        
        for i in trust:
            count[i[1]] += 1
            count[i[0]] -= 1
            
        for i in count:
            if count[i] == n-1:
                return i
                
            
        return -1