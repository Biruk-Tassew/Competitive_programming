class Solution:
    def robotWithString(self, s: str) -> str:
        s_count = Counter(s)
        t_stack = []
        p_stack = []
        
        
        for i in s:
            t_stack.append(i)
            
            if s_count[i] == 1:
                del s_count[i] 
            else:
                s_count[i] -= 1
                 
                
            while s_count and t_stack and t_stack[-1] <= min(s_count):
                p_stack.append(t_stack.pop())
            
                
        return "".join(p_stack + t_stack[::-1])
            
        
        