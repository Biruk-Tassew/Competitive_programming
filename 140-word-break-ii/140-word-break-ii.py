class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        wordDict = set(wordDict)
        cur = []
        ans = []
        
        def backtrack(s_idx, e_idx):
            if e_idx == len(s):
                if s[s_idx:e_idx] in wordDict:
                    cur.append(s[s_idx:e_idx])
                    ans.append(" ".join(cur))
                    cur.pop()
                return 
            
            if s[s_idx:e_idx] in wordDict:
                cur.append(s[s_idx:e_idx])
                backtrack(e_idx, e_idx+1)
                cur.pop()
                
            backtrack(s_idx, e_idx+1)
            
        backtrack(0, 1)
        return ans
            