class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letters = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        self.backtrack(0, "", res, digits)
        return res
    
    def backtrack(self, idx, cur_comb, res, digits):
        if idx == len(digits):
            if cur_comb:
                res.append(cur_comb)
            return
        
        for i in range(len(self.letters[digits[idx]])):
            cur_comb += self.letters[digits[idx]][i]
            
            self.backtrack(idx+1, cur_comb, res, digits)
            
            cur_comb = cur_comb[:-1]