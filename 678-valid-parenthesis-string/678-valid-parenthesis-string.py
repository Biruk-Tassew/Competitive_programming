class Solution:
    def checkValidString(self, s: str) -> bool:
        
        opening = 0
        closing = 0
        
        for i in s:
            if i == "(":
                opening += 1
            else:
                opening -= 1
                
            if i == ")":
                closing -= 1
            else:
                closing += 1
                
            if closing < 0:
                break
                
            opening = max(opening, 0)
            
        return not opening
        
        
        
                    
                