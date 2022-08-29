class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        for i in range(len(s)):
            last_occ[s[i]] = i
            
        visited = set()
        stack = [""]
        
        for i in range(len(s)):
            if s[i] in visited:
                continue
                
            while stack[-1] > s[i] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
                
            visited.add(s[i])
            stack.append(s[i])
            
            
        return "".join(stack)
   
