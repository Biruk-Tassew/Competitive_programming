class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] in {"(", ")"}:
                if stack and stack[-1][0] == "(" and s[i] == ")":
                    stack.pop()
                else:
                    stack.append((s[i],i))
                    
        s = list(s)
        devi = 0
        for i in stack:
            s.pop(i[1]-devi)
            devi += 1
        return s