class Solution:
    def calculate(self, s: str) -> int:
        
        curNum = 0
        curSign = '+'
        stack = []
        operators = ["+", "-", "*", "/"]
        
        for i in range(len(s)):

            if s[i].isdigit():
                curNum = curNum * 10+int(s[i])
                
            if  s[i] in operators or i + 1 == len(s):
                if curSign == '+':
                    stack.append(curNum)
                elif curSign== '-':
                    stack.append(-1 * curNum)
                elif curSign == '*':
                    stack[-1] *= curNum
                elif curSign == '/':
                    stack[-1] = int(stack[-1]/float(curNum))
                curSign = s[i]
                curNum = 0
        return sum(stack)
