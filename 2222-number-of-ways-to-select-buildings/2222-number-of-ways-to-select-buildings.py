class Solution:
    def numberOfWays(self, s: str) -> int:
        count = Counter(s)
        
        zeros = 1 if s[0]=="0" else 0
        ones = 1 if s[0]=="1" else 0
        res = 0
        
        for i in range(1, len(s)-1):
            if s[i] == "0":
                zeros += 1
                res += ones * (count["1"] - ones) 
            else:
                ones += 1
                res += zeros * (count["0"] - zeros) 
                
        return res
                
                
        
   