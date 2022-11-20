class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = 0
        watch_loss = 0
        st_idx = 0
        
        for i in range(len(gas)):
            net += gas[i]-cost[i]
            watch_loss += gas[i]-cost[i]
            
            if watch_loss < 0:
                st_idx = i+1
                watch_loss = 0
                
        if net < 0:
            return -1
        
        return st_idx