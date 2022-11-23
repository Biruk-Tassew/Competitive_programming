class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        que = deque([start])
        visited = set([start])
        level = 0
        
        while que:
            for _ in range(len(que)):
                cur_num = que.popleft()
                
                for num in nums:
                    for n_num in {cur_num-num, cur_num+num, cur_num^num}:
                        if n_num == goal:
                            return level+1
                        if 0 <= n_num <= 1000 and n_num not in visited:
                            que.append(n_num)
                            visited.add(n_num)
                            
            level += 1
            
        return -1