class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i.isdigit() or len(i) > 1:
                stack.append(i)
            else:
                opd_one = stack.pop()
                opd_two = stack.pop()
                if i == "+":
                    stack.append(str(int(opd_two)+int(opd_one)))
                elif i == "-":
                    stack.append(str(int(opd_two)-int(opd_one)))
                elif i == "*":
                    stack.append(str(int(opd_two)*int(opd_one)))
                else:
                    if int(opd_one) * int(opd_two) < 0:
                        stack.append(str(-1*(int(opd_two)//(-1*int(opd_one)))))
                    else:
                        stack.append(str(int(opd_two)//int(opd_one)))
                        
                
        return int(stack[-1])