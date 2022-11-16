class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        
        opening = 0
        closing = 0
        
        for i in range(len(s)):
            if s[i] == "(" or locked[i] == "0":
                opening += 1
            else:
                opening -= 1
                
            if opening < 0:
                return False
            
        for i in range(len(s)-1, -1, -1):
            if s[i] == ")" or locked[i] == "0":
                closing += 1
            else:
                closing -= 1
                
            if closing < 0:
                return False
        
                
        return True