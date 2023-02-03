class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splited_path = path.split("/")
        
        for i in splited_path:
            
            if i not in {"", "."}:
                if i == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
                    
        return "/" + "/".join(stack)