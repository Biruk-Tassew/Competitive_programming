class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM_dict = {}
        
        for log in logs:
            if log[0] in UAM_dict and log[1] not in UAM_dict[log[0]][1]:
                UAM_dict[log[0]][0] += 1
                UAM_dict[log[0]][1].add(log[1])
            elif log[0] not in UAM_dict:
                UAM_dict[log[0]] = [1, set([log[1]])]
                
                
        res = [0]*k
        for uam in UAM_dict:
            res[UAM_dict[uam][0]-1] += 1
            
        return res