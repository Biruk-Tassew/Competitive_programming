class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        cur_num = 0
        sign = 1
        stack = []
        
        for i in s:
            if i.isdigit():
                cur_num = cur_num*10 + int(i)
            elif i == "+" or i == "-":
                res += sign*cur_num
                cur_num = 0
                sign = int(i+"1")
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif i == ")":
                res += sign*cur_num
                cur_num = 0
                
                res *= stack.pop()
                res += stack.pop()
                
        if cur_num != 0:
            res += sign*cur_num
            
        return res