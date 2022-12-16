class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        que = deque([s])
        ans = s
        visited = set([s])
        
        
        while que:
            s = que.popleft()
            ans = min(ans, s)
            summ = ""
            for i in range(len(s)):
                if i % 2:
                    summ += str((int(s[i])+a)%10)
                else:
                    summ += s[i]  
            if summ not in visited:
                que.append(summ)
                visited.add(summ)
            if s[-b:]+s[:-b] not in visited:
                que.append(s[-b:]+s[:-b])
                visited.add(s[-b:]+s[:-b])
                
        return ans 
            