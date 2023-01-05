class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] in {"(", ")"}:
                if stack and stack[-1][0] == "(" and s[i] == ")":
                    stack.pop()
                else:
                    stack.append((s[i], i))
                    
        to_be_jumped = set()
        for i in stack:
            to_be_jumped.add(i[1])
            
        ans = ""
        for i in range(len(s)):
            if i not in to_be_jumped:
                ans += s[i]
                
        return ans