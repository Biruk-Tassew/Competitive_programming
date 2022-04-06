class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens)==1:
            return tokens[0]
        comp = []
        for i in tokens:
            if not(i == "+" or i == "-" or i == "*" or i == "/"):
                comp.append(i)

            else:
                outPut = 0
                operand_2 = comp.pop()
                operand_1 = comp.pop()
                
                outPut = eval(str(operand_1) + i + str(operand_2))
                if i == '/':
                    outPut = math.trunc(outPut)
                comp.append(outPut)
                    
        return comp.pop()
