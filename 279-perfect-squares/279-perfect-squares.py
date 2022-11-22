class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = set([i**2 for i in range(n//2 + 1)])
        que = deque([n])
        visited = set([n])
        count = 0
        
        while que:
            for _ in range(len(que)):
                num = que.popleft()
                
                if num in sqrs:
                    return count+1
                    
                for i in sqrs:
                    if num > i in sqrs and num-i not in visited:
                        visited.add(num-i)
                        que.append(num-i)
            count += 1
        return count