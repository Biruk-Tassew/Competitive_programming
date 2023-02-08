class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        conn_cnt = defaultdict(lambda: 0)
        connection = defaultdict(list)
        
        for edge in adjacentPairs:
            conn_cnt[edge[0]] += 1
            conn_cnt[edge[1]] += 1
            
            connection[edge[0]].append(edge[1])
            connection[edge[1]].append(edge[0])
            
        
        temp = float('inf')
        for i in conn_cnt:
            if conn_cnt[i] == 1 and i < temp:
                temp = i     
        ans = [temp]
                
        while len(ans) < len(adjacentPairs)+1:
            for node in connection[ans[-1]]:
                if len(ans) > 1 and node == ans[-2]:
                    continue
                    
                ans.append(node)
                break
                
        return ans
        