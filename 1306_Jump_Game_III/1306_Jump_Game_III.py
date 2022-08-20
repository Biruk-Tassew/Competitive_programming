class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        que = deque([start])
        visited = set()
        
        while que:
            idx = que.popleft()
            left_idx = idx - arr[idx]
            right_idx = idx + arr[idx]
            
        
            if 0 <= left_idx < len(arr) and left_idx not in visited:
                que.append(left_idx)
                visited.add(left_idx)
            if 0 <= right_idx < len(arr) and right_idx not in visited:
                que.append(right_idx)
                visited.add(right_idx)
                
            if not arr[idx]:
                return True
            
        return False
