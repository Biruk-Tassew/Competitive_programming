class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans = (0,0) 
        count = defaultdict(int) 
        
        for log in logs: 
            for i in range(int(log[0]), int(log[1])): 
                count[i] += 1 
                if count[i] > ans[1]: 
                    ans = (i, count[i]) 
                    
                if count[i] == ans[1] and i < ans[0]: 
                    ans = (i, count[i])
                
        return ans[0]