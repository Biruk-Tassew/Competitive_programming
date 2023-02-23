class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.solve(expression)
        
    def solve(self, expression):
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        
        for i in range(len(expression)):
            if not expression[i].isdigit():
                left_exps = self.solve(expression[:i])
                right_exps = self.solve(expression[i+1:])
                
                for left in left_exps:
                    for right in right_exps:
                        res.append(eval(str(left) + expression[i] + str(right)))
                        
        return res