class Solution:
    def romanToInt(self, s: str) -> int:
        nums_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0
        
        for i in range(len(s)-1):
            if nums_dict[s[i]] < nums_dict[s[i+1]]:
                num -= nums_dict[s[i]]
            else:
                num += nums_dict[s[i]]
                
        return num + nums_dict[s[len(s)-1]]